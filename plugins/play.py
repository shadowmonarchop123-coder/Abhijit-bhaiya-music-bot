import asyncio
from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.streamer import play_next
from core.queues import add, is_empty, clear

from core.prefetch import extract_async, prefetch

from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall


@app.on_message(filters.command(["play", "p"]) & filters.group)
async def play_cmd(_, message: Message):
    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ Usage: /play song name")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡ Processing...")

    try:
        # ⚡ TURBO extract (search + stream url in one hit)
        data = await extract_async(query)
    except Exception as e:
        return await msg.edit(f"❌ Stream error\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    first = is_empty(chat_id)
    add(chat_id, song)

    # 🔥 background prefetch (next instant)
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
