import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
from core.call import call_py
from core.queues import pop, get, is_empty
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    await call_py.join_group_call(
        chat_id,
        InputStream(
            AudioPiped(
                file_path,
                ffmpeg_parameters=FFMPEG_COMMAND
            )
        ),
    )

async def play_next(chat_id):
    pop(chat_id)
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        return

    next_track = get(chat_id)
    await start_stream(chat_id, next_track["file"])
