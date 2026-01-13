import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls.types import StreamType 
from core.call import call_py
from core.queues import pop, get, is_empty
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    try:
        # Pehle join karne ki koshish karega
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
        # Agar assistant already call mein hai, toh stream change karega (Fastest Way)
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
    pop(chat_id)
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except Exception:
            pass
        return

    next_track = get(chat_id)
    # Priority 'url' ko di gayi hai direct extraction ke liye
    file_to_stream = next_track.get("url") or next_track.get("file")
    
    if not file_to_stream:
        return

    try:
        await start_stream(chat_id, file_to_stream)
    except Exception as e:
        print(f"Streaming Error: {e}")
