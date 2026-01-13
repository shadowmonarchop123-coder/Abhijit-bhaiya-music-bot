from pyrogram import filters
from pyrogram.types import Message
from core.client import app
# core/queues se sahi variable (queues) import kiya
from core.queues import queues, is_empty 

@app.on_message(filters.command(["queue", "q"]) & filters.group)
async def queue_cmd(_, message: Message):
    chat_id = message.chat.id

    # Check if queue is empty
    if is_empty(chat_id):
        return await message.reply("📭 **Queue empty hai.**")

    text = "📜 **Current Queue:**\n\n"
    
    # current_queue ko safely access karein
    current_queue = queues.get(chat_id, [])
    
    # List slicing for top 15 songs
    for i, song in enumerate(list(current_queue)[:15], start=1):
        title = song.get('title', 'Unknown Track')
        if i == 1:
            text += f"▶️ **Now Playing:**\n└ {title}\n\n"
            if len(current_queue) > 1:
                text += "📋 **Up Next:**\n"
        else:
            text += f"{i-1}. {title}\n"

    # Total count footer
    if len(current_queue) > 15:
        text += f"\n...aur {len(current_queue) - 15} aur gaane hain."

    await message.reply(text, disable_web_page_preview=True)
