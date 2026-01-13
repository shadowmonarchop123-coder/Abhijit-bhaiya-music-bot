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

# -------- ULTRA FAST SEARCH --------
def yt_search(q):
    try:
        # Sirf 1 result aur direct link ke liye
        search = VideosSearch(q, limit=1)
        r = search.result()
        if r and "result" in r and len(r["result"]) > 0:
            return r["result"][0]["link"]
        return None
    except Exception:
        return None

# -------- LIGHTWEIGHT EXTRACTOR --------
def yt_stream(url):
    if not url:
        raise Exception("Invalid Link")
        
    cookie_path = "cookies.txt"
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "bestaudio/best",
        "skip_download": True,
        "noprogress": True,
        "proxy": None, # Fixes proxies error
        # 🔥 Speed Boost Settings
        "extract_flat": True,
        "lazy_playlist": True,
        "cachedir": False,
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    }

    if os.path.exists(cookie_path):
        ydl_opts["cookiefile"] = cookie_path

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # process=False se extraction instant hoti hai
            info = ydl.extract_info(url, download=False, process=False)
            return {
                "title": info.get("title", "Music"),
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
    msg = await message.reply("⚡") 

    try:
        loop = asyncio.get_event_loop()

        # 1. Search (Fixed String Issue)
        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
            if not link:
                return await msg.edit("❌ No results found.")
        else:
            link = query

        # 2. Fast Extraction
        data = await loop.run_in_executor(None, yt_stream, link)

    except Exception as e:
        return await msg.edit(f"❌ Error: {e}")

    song = {"title": data["title"], "url": data["url"]}
    
    # Queue management
    first = is_empty(chat_id)
    add(chat_id, song)

    if first:
        try:
            await play_next(chat_id)
            await msg.delete()
            await message.reply(f"▶️ **Started:** {data['title']}")
        except Exception as e:
            clear(chat_id)
            await msg.edit(f"❌ VC Error: {e}")
    else:
        await msg.edit(f"➕ **Queued:** {data['title']}")
