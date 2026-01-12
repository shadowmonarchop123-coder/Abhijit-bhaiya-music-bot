import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
# Yahan se call_py ka import hata diya hai loop break karne ke liye
from core.queues import add, get, pop, is_empty, clear

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls import StreamType
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch
import yt_dlp


# ---------------- FAST SEARCH ----------------
def yt_search(query: str):
    search = VideosSearch(query, limit=1)
    result = search.result()
    if not result["result"]:
        return None
    return result["result"][0]["link"]


# ---------------- FAST DIRECT STREAM ----------------
def yt_stream(url: str):
    ydl_opts = {
        "format": "bestaudio",
        "quiet": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
        "cookiefile": "cookies.txt",
        "extractor_args": {"youtube": {"player_client": ["android"]}},
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if "entries" in info:
            info = info["entries"][0]

        return {
            "title": info.get("title", "Unknown"),
            "url": info["url"]
        }


# ---------------- VC PLAYER ----------------
async def play_next(chat_id: int):
    # Local import loop break karne ke liye
    from core.call import call_py 
    
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
        await call_py.change_stream(
            chat_id,
            AudioPiped(song["url"])
        )


# ---------------- PLAY COMMAND ----------------
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    # Yahan bhi call_py chahiye hoga agar play_next call ho raha hai
    from core.call import call_py
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    m = await message.reply("⚡ Processing...")

    try:
        loop = asyncio.get_event_loop()

        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
            if not link:
                return await m.edit("❌ No results found.")
        else:
            link = query

        data = await loop.run_in_executor(None, yt_stream, link)

    except Exception as e:
        return await m.edit(f"❌ Stream error\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    first_song = is_empty(chat_id)
    add(chat_id, song)

    if first_song:
        try:
            await play_next(chat_id)
            await m.edit(f"▶️ <b>Now Playing:</b> {data['title']}")
        except (GroupCallNotFound, NoActiveGroupCall):
            clear(chat_id)
            await m.edit("❌ Voice chat start karo aur assistant add karo.")
    else:
        await m.edit(f"➕ <b>Queued:</b> {data['title']}")
