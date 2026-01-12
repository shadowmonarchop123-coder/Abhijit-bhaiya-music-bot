from pyrogram import filters
from core.client import app
from core.queues import queues

@app.on_message(filters.command("queue") & filters.group)
async def queue_cmd(_, message):
    chat_id = message.chat.id

    if chat_id not in queues or not queues[chat_id]:
        return await message.reply("📭 Queue empty hai.")

    text = "📜 <b>Current Queue:</b>\n\n"
    for i, song in enumerate(list(queues[chat_id])[:10], start=1):
        text += f"{i}. {song['title']}\n"

    await message.reply(text)
