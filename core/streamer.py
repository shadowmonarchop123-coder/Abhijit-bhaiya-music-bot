import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls.types import StreamType 
from core.call import call_py
from core.queues import get, is_empty, pop
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    try:
        await call_py.join_group_call(
            chat_id,
            InputStream(AudioPiped(file_path, ffmpeg_parameters=FFMPEG_COMMAND)),
            stream_type=StreamType().pulse_stream 
        )
    except Exception:
        await call_py.change_stream(
            chat_id,
            InputStream(AudioPiped(file_path, ffmpeg_parameters=FFMPEG_COMMAND))
        )

async def play_next(chat_id):
    pop(chat_id)
    if is_empty(chat_id):
        try: await call_py.leave_group_call(chat_id)
        except: pass
        return

    next_track = get(chat_id)
    if next_track:
        await start_stream(chat_id, next_track.get("url"))
