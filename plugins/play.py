import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.streamer import play_next
from core.queues import add, is_empty, clear
from core.prefetch import prefetch

from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall

from youtubesearchpython import VideosSearch
from core.prefetch import _extract as yt_stream
from core.prefetch import extract_async, prefetch


def yt_search(q):
    search = VideosSearch(q, limit=1)
    r = search.result()
    if not r["result"]:
        return None
    return r["result"][0]["link"]


@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡ Processing...")

    try:
        data = await extract_async(query)
    except Exception as e:
        return await msg.edit(f"❌ Stream error\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    first = is_empty(chat_id)
    add(chat_id, song)

    # 🔥 instant next preload
    asyncio.create_task(prefetch(chat_id, query))

    if first:
        try:
            await play_next(chat_id)
            await msg.edit(f"▶️ <b>Now Playing:</b> {data['title']}")
        except (GroupCallNotFound, NoActiveGroupCall):
            clear(chat_id)
            await msg.edit("❌ VC start karo aur assistant add karo.")
    else:
        await msg.edit(f"➕ <b>Queued:</b> {data['title']}")
