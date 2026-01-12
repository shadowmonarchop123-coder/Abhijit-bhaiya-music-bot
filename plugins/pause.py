from pyrogram import filters
from core.client import app
from core.call import call_py

@app.on_message(filters.command("pause") & filters.group)
async def pause_cmd(_, message):
    try:
        await call_py.pause_stream(message.chat.id)
        await message.reply("⏸ Music paused.")
    except:
        await message.reply("❌ Koi music play nahi ho raha.")
