import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.streamer import play_next
from core.queues import add, is_empty, clear

from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch
import yt_dlp


def yt_search(q):
    search = VideosSearch(q, limit=1)
    r = search.result()
    if not r["result"]:
        return None
    return r["result"][0]["link"]


def yt_stream(url):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "cookiefile": "cookies.txt",
        "format": "bestaudio/best",
        "skip_download": True,
        "nocheckcertificate": True,
        "geo_bypass": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        if "entries" in info:
            info = info["entries"][0]

        return {
            "title": info.get("title", "Unknown"),
            "url": info["url"]
        }


@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ /play song name")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡ Turbo processing...")

    try:
        loop = asyncio.get_event_loop()

        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
            if not link:
                return await msg.edit("❌ No result found")
        else:
            link = query

        data = await loop.run_in_executor(None, yt_stream, link)

    except Exception as e:
        return await msg.edit(f"❌ Stream error\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    first = is_empty(chat_id)
    add(chat_id, song)

    if first:
        try:
            await play_next(chat_id)
            await msg.edit(f"▶️ <b>Now Playing:</b> {data['title']}")
        except (GroupCallNotFound, NoActiveGroupCall):
            clear(chat_id)
            await msg.edit("❌ VC start karo aur assistant add karo")
    else:
        await msg.edit(f"➕ <b>Queued:</b> {data['title']}")
