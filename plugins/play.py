import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.call import call_py
from core.queues import add, get, pop, is_empty

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls import StreamType
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch
import yt_dlp


# ----------- YT STREAM URL -----------
def yt_stream(query: str):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if "entries" in info:
            info = info["entries"][0]
        return {
            "title": info.get("title"),
            "url": info["url"]
        }


def yt_search(query: str):
    search = VideosSearch(query, limit=1)
    result = search.result()
    if not result["result"]:
        return None
    data = result["result"][0]
    return data["link"]


# ----------- PLAYER -----------
async def play_next(chat_id: int):
    if is_empty(chat_id):
        return

    song = get(chat_id)

    await call_py.join_group_call(
        chat_id,
        AudioPiped(song["url"]),
        stream_type=StreamType().pulse_stream
    )


# ----------- COMMAND -----------
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    m = await message.reply("🔎 Searching...")

    try:
        if not query.startswith("http"):
            link = await asyncio.get_event_loop().run_in_executor(None, yt_search, query)
            if not link:
                return await m.edit("❌ No results found.")
        else:
            link = query

        data = await asyncio.get_event_loop().run_in_executor(None, yt_stream, link)

    except Exception as e:
        return await m.edit(f"❌ Stream error\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    add(chat_id, song)

    if len(get(chat_id)) == 1:
        try:
            await play_next(chat_id)
            await m.edit(f"▶️ Now playing: <b>{data['title']}</b>")
        except (GroupCallNotFound, NoActiveGroupCall):
            await m.edit("❌ Pehle voice chat start karo.")
    else:
        await m.edit(f"➕ Added to queue: <b>{data['title']}</b>")
