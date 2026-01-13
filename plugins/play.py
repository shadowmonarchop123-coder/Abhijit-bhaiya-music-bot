import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.call import call_py
from core.queues import add, get, is_empty, clear

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls import StreamType
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch
import yt_dlp


# -------- FAST SEARCH --------
def yt_search(q):
    search = VideosSearch(q, limit=1)
    r = search.result()
    if not r["result"]:
        return None
    return r["result"][0]["link"]


# -------- FIXED STRONG STREAM EXTRACTOR --------
def yt_stream(url):
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "format": "bestaudio",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "skip_download": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

        if "entries" in info:
            info = info["entries"][0]

        formats = info.get("formats", [])

        audio = None
        for f in formats:
            if f.get("acodec") != "none" and f.get("url"):
                audio = f
                break

        if not audio:
            raise Exception("No playable audio format found")

        return {
            "title": info.get("title", "Unknown"),
            "url": audio["url"]
        }


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
    except:
        await call_py.change_stream(
            chat_id,
            AudioPiped(song["url"])
        )


# -------- COMMAND --------
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡ Processing...")

    try:
        loop = asyncio.get_event_loop()

        if not query.startswith("http"):
            link = await loop.run_in_executor(None, yt_search, query)
            if not link:
                return await msg.edit("❌ No results found.")
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
            await msg.edit("❌ VC start karo aur assistant add karo.")
    else:
        await msg.edit(f"➕ <b>Queued:</b> {data['title']}")
