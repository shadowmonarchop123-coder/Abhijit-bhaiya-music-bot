import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
# 🔥 Sahi import v0.9.7 ke liye
from pytgcalls.types import StreamType 
from core.call import call_py
from core.queues import get, is_empty, pop
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    try:
        # Puraani library mein StreamType().pulse_stream sahi method hai
        await call_py.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(
                    file_path,
                    ffmpeg_parameters=FFMPEG_COMMAND 
                )
            ),
            stream_type=StreamType().pulse_stream 
        )
    except Exception:
        # Agar Assistant already VC mein hai toh stream change karein
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
        # Extraction ke liye url pass karein
        file_to_stream = next_track.get("url") or next_track.get("file")
        await start_stream(chat_id, file_to_stream)
