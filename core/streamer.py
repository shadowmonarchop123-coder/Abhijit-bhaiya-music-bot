import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls.types import StreamType # ✨ Fast streaming ke liye
from core.call import call_py
from core.queues import pop, get, is_empty
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    # 'file_path' yahan YouTube ka direct URL hoga jo play.py se aa raha hai
    await call_py.join_group_call(
        chat_id,
        InputStream(
            AudioPiped(
                file_path,
                # FFMPEG_COMMAND ko config.py mein optimize karein
                ffmpeg_parameters=FFMPEG_COMMAND 
            )
        ),
        # Pulse stream sabse fast response deta hai
        stream_type=StreamType().pulse_stream 
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
    # Ensure hum 'url' bhej rahe hain agar direct streaming hai
    file_to_stream = next_track.get("url") or next_track.get("file")
    
    try:
        await start_stream(chat_id, file_to_stream)
    except Exception as e:
        print(f"Streaming Error: {e}")
