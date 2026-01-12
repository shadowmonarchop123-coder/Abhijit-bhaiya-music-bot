from pyrogram import filters
from core.client import app
from core.call import call_py

@app.on_message(filters.command("resume") & filters.group)
async def resume_cmd(_, message):
    try:
        await call_py.resume_stream(message.chat.id)
        await message.reply("▶️ Music resumed.")
    except:
        await message.reply("❌ Koi music paused nahi hai.")
