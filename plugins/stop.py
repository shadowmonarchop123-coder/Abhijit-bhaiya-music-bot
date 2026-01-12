from pyrogram import filters
from core.client import app
from core.call import call_py
from core.queues import clear

@app.on_message(filters.command("stop") & filters.group)
async def stop_cmd(_, message):
    chat_id = message.chat.id
    try:
        clear(chat_id)
        await call_py.leave_group_call(chat_id)
        await message.reply("⏹ Music stopped & VC left.")
    except:
        await message.reply("❌ Koi active VC nahi mila.")
