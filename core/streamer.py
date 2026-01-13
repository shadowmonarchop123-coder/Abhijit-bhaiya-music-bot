import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
# Sahi import version 0.9.7 ke liye:
from pytgcalls.types import StreamType 
from core.call import call_py
from core.queues import get, is_empty, pop
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    try:
        await call_py.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(
                    file_path,
                    ffmpeg_parameters=FFMPEG_COMMAND 
                )
            ),
            # Yahan check karein ki StreamType() call ho raha hai
            stream_type=StreamType().pulse_stream 
        )
    except Exception as e:
        # Agar Assistant pehle se join hai
        await call_py.change_stream(
            chat_id,
            InputStream(
                AudioPiped(
                    file_path,
                    ffmpeg_parameters=FFMPEG_COMMAND 
                )
            )
        )

async def play_next(chat_id):
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        return

    next_track = get(chat_id)
    if next_track:
        await start_stream(chat_id, next_track.get("url"))
