import asyncio
import os
import yt_dlp
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from core.client import app
from core.call import call_py
from core.queues import add, get, is_empty, clear

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls import StreamType
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

# -------- FAST SEARCH --------
async def yt_search(q):
    search = VideosSearch(q, limit=1)
    # yahan await ki zaroorat nahi agar library async nahi hai, 
    # par executor ke andar dalna behtar hai
    r = search.result()
    if not r["result"]:
        return None
    return r["result"][0]["link"]

# -------- SUPER FAST EXTRACTOR --------
def yt_stream(url):
    cookie_path = "cookies.txt"
    
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "bestaudio/best",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "skip_download": True,
        "proxy": None,
        # 🔥 Fast processing options
        "extract_flat": "in_playlist", # Playlist ko skip karega
        "force_generic_extractor": False,
        "cachedir": False,
        "youtube_include_dash_manifest": False, 
        "youtube_include_hls_manifest": False,
        "noprogress": True,
    }

    if os.path.exists(cookie_path):
        ydl_opts["cookiefile"] = cookie_path

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # process=True aur download=False se direct link jaldi milta hai
            info = ydl.extract_info(url, download=False)
            if "entries" in info:
                info = info["entries"][0]
            
            return {
                "title": info.get("title", "Unknown"),
                "url": info.get("url") 
            }
        except Exception as e:
            raise Exception(f"YT-DLP Error: {str(e)}")

# -------- VC PLAYER --------
async def play_next(chat_id):
    if is_empty(chat_id):
        return
    song = get(chat_id)
    try:
        await call_py.join_group_call(
            chat_id,
            AudioPiped(song["url"]),
            stream_type=StreamType().pulse_stream
        )
    except Exception:
        try:
            await call_py.change_stream(chat_id, AudioPiped(song["url"]))
        except Exception:
            pass

# -------- COMMAND --------
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡") # Small text = fast UI feel

    try:
        loop = asyncio.get_event_loop()

        # 1. Faster Search
        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
            if not link:
                return await msg.edit("❌ No results found.")
        else:
            link = query

        # 2. Faster Extraction
        data = await loop.run_in_executor(None, yt_stream, link)

    except Exception as e:
        return await msg.edit(f"❌ Error: {e}")

    song = {"title": data["title"], "url": data["url"]}
    first = is_empty(chat_id)
    add(chat_id, song)

    if first:
        try:
            await play_next(chat_id)
            # Delete processing message for clean look
            await msg.delete()
            await message.reply(f"▶️ **Now Playing:** {data['title']}")
        except Exception as e:
            clear(chat_id)
            await msg.edit(f"❌ VC Error: {e}")
    else:
        await msg.edit(f"➕ **Queued:** {data['title']}")
