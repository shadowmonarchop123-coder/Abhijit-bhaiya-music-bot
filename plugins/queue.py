from pyrogram import filters
from pyrogram.types import Message
from core.client import app
from core.queues import get, is_empty # core/queues se optimized functions use karein

# Note: queues ko direct import karne ke bajaye helper functions use karna safe hai
from core.queues import queue as queues 

@app.on_message(filters.command(["queue", "q"]) & filters.group)
async def queue_cmd(_, message: Message):
    chat_id = message.chat.id

    # Check if queue is empty using the helper function
    if chat_id not in queues or not queues[chat_id]:
        return await message.reply("📭 **Queue empty hai.**")

    # Fast response ke liye processing message ki zarurat nahi, direct reply karein
    text = "📜 **Current Queue:**\n\n"
    
    # List slicing fast hoti hai, lekin enumeration ko optimize kiya hai
    current_queue = queues[chat_id]
    
    for i, song in enumerate(current_queue[:15], start=1): # 10 ki jagah 15 dikhana behtar hai
        title = song.get('title', 'Unknown Track')
        if i == 1:
            text += f"▶️ **Now Playing:**\n└ {title}\n\n"
            if len(current_queue) > 1:
                text += "📋 **Up Next:**\n"
        else:
            text += f"{i-1}. {title}\n"

    # Agar 15 se zyada gaane hain toh total count dikhayein
    if len(current_queue) > 15:
        text += f"\n...aur {len(current_queue) - 15} aur gaane hain."

    await message.reply(text, disable_web_page_preview=True)
