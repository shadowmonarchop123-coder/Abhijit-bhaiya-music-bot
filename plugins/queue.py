from pyrogram import filters
from pyrogram.types import Message

from core.client import app
from core.queues import queues


@app.on_message(filters.command(["queue", "q"]) & filters.group)
async def queue_cmd(_, message: Message):
    chat_id = message.chat.id

    if chat_id not in queues or len(queues[chat_id]) == 0:
        return await message.reply("📭 <b>Queue empty hai.</b>")

    text = "📜 <b>Current Queue:</b>\n\n"

    for i, song in enumerate(list(queues[chat_id])[:10], start=1):
        if i == 1:
            text += f"▶️ <b>Now Playing:</b> {song['title']}\n\n"
        else:
            text += f"{i-1}. {song['title']}\n"

    await message.reply(text, disable_web_page_preview=True)
