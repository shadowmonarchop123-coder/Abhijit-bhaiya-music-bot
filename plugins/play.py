import asyncio
import os
import yt_dlp
import traceback
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from core.client import app
from core.call import call_py
from core.queues import add, get, is_empty, clear

# --- ULTRA FAST SEARCH ---
def yt_search(q):
    try:
        search = VideosSearch(q, limit=1)
        r = search.result()
        if r and "result" in r and len(r["result"]) > 0:
            return r["result"][0]["link"]
        return None
    except Exception:
        return None

# --- EXTRACTION FIX ---
def yt_stream(url):
    ydl_opts = {
        "quiet": True,
        "format": "bestaudio/best",
        "skip_download": True,
        "extract_flat": False, # Isse URL sahi se extract hogi
        "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title", "Music"),
                "url": info.get("url") 
            }
        except Exception as e:
            raise Exception(f"YT-DLP Error: {str(e)}")

# --- COMMAND ---
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡ **Searching...**") 

    try:
        loop = asyncio.get_event_loop()
        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
        else:
            link = query

        if not link:
            return await msg.edit("❌ No results found.")

        data = await loop.run_in_executor(None, yt_stream, link)
    except Exception as e:
        return await msg.edit(f"❌ Error: {e}")

    song = {"title": data["title"], "url": data["url"]}
    first = is_empty(chat_id)
    add(chat_id, song)

    if first:
        try:
            # Lazy import to avoid circular dependency
            from core.streamer import start_stream
            await start_stream(chat_id, data["url"])
            await msg.delete()
            await message.reply(f"▶️ **Started:** {data['title']}")
        except Exception as e:
            clear(chat_id)
            traceback.print_exc()
            await msg.edit(f"❌ VC Error: {e}")
    else:
        await msg.edit(f"➕ **Queued:** {data['title']}")
