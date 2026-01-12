from pyrogram import filters
from core.client import app
from core.call import call_py
from core.queues import pop, is_empty, get
from pytgcalls.types.input_stream import InputStream, InputAudioStream

async def play_next(chat_id: int):
    if is_empty(chat_id):
        await call_py.leave_group_call(chat_id)
        return

    song = get(chat_id)
    await call_py.change_stream(
        chat_id,
        InputStream(
            InputAudioStream(song["file"])
        )
    )

@app.on_message(filters.command("skip") & filters.group)
async def skip_cmd(_, message):
    chat_id = message.chat.id

    try:
        pop(chat_id)
        if is_empty(chat_id):
            await call_py.leave_group_call(chat_id)
            return await message.reply("📭 Queue khatam. VC left.")

        await play_next(chat_id)
        await message.reply("⏭ Skipped. Next song playing.")
    except:
        await message.reply("❌ Skip nahi ho paya.")
