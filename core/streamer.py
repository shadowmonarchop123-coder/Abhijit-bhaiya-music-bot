import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
# PyTgCalls v0.9.7 ke liye sahi imports
from pytgcalls import StreamType 
from core.call import call_py
from core.queues import get, is_empty, pop

async def start_stream(chat_id, file_path):
    try:
        # v0.9.7 mein ffmpeg_parameters support nahi hai, ise hata diya gaya hai
        await call_py.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(file_path)
            ),
            stream_type=StreamType.pulse_stream 
        )
    except Exception as e:
        # Agar pehle se join hai toh sirf stream badlein
        try:
            await call_py.change_stream(
                chat_id,
                InputStream(
                    AudioPiped(file_path)
                )
            )
        except Exception as ex:
            print(f"❌ VC Error: {ex}")

async def play_next(chat_id):
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        return

    next_track = get(chat_id)
    if next_track:
        file_to_stream = next_track.get("url") or next_track.get("file")
        await start_stream(chat_id, file_to_stream)
