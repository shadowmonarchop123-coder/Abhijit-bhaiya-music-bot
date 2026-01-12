from pyrogram import filters
from core.client import app
from config import BOT_NAME

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text(
        f"🎵 <b>{BOT_NAME}</b>\n\n"
        "VC Music Bot ready!\n\n"
        "Commands:\n"
        "/play song name or link\n"
        "/pause\n/resume\n/skip\n/stop\n/queue"
    )
