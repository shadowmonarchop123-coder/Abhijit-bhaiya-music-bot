import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.call import call_py
from core.queues import add, get, pop, is_empty
from core.downloader import download_audio

from pytgcalls.types.input_stream import AudioPiped
from pytgcalls import StreamType
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch


# ---------- helper ----------
def yt_search(query: str):
    search = VideosSearch(query, limit=1)
    result = search.result()
    if not result["result"]:
        return None
    data = result["result"][0]
    return {
        "title": data["title"],
        "link": data["link"]
    }


async def play_next(chat_id: int):
    if is_empty(chat_id):
        return

    song = get(chat_id)
    file_path = song["file"]

    await call_py.join_group_call(
        chat_id,
        AudioPiped(file_path),
        stream_type=StreamType().pulse_stream
    )


# ---------- command ----------
@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    m = await message.reply("🔎 Searching...")

    if not query.startswith("http"):
        data = await asyncio.get_event_loop().run_in_executor(None, yt_search, query)
        if not data:
            return await m.edit("❌ No results found.")
        url = data["link"]
        title = data["title"]
    else:
        url = query
        title = "Audio"

    await m.edit("📥 Downloading...")

    try:
        file_path, _ = await asyncio.get_event_loop().run_in_executor(
            None, download_audio, url
        )
    except Exception as e:
        return await m.edit(f"❌ Download error\n<code>{e}</code>")

    song = {"title": title, "file": file_path}
    add(chat_id, song)

    if len(os.listdir("downloads")) == 1:
        try:
            await play_next(chat_id)
            await m.edit(f"▶️ Now playing: <b>{title}</b>")
        except (GroupCallNotFound, NoActiveGroupCall):
            await m.edit("❌ Pehle voice chat start karo.")
    else:
        await m.edit(f"➕ Added to queue: <b>{title}</b>")
