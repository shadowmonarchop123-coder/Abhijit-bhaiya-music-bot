import asyncio
import os
import yt_dlp
import traceback # Error detail ke liye
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from core.client import app
from core.call import call_py
from core.queues import add, get, is_empty, clear

# Streamer se functions import karein taaki duplicate logic na ho
from core.streamer import start_stream 

# -------- ULTRA FAST SEARCH --------
def yt_search(q):
    try:
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
        "extract_flat": True, # Fast extraction
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

        # 1. Search
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

    if not data.get("url"):
        return await msg.edit("❌ Streaming URL nahi mil saki.")

    song = {"title": data["title"], "url": data["url"]}
    first = is_empty(chat_id)
    add(chat_id, song)

    if first:
        try:
            # core/streamer.py ka start_stream use karein jisme error catching hai
            from core.streamer import start_stream
            await start_stream(chat_id, data["url"])
            
            await msg.delete()
            await message.reply(f"▶️ **Started:** {data['title']}")
        except Exception as e:
            clear(chat_id)
            print(f"❌ Play Command Error: {e}")
            traceback.print_exc()
            await msg.edit(f"❌ VC Error: {e}")
    else:
        await msg.edit(f"➕ **Queued:** {data['title']}")
