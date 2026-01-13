import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
# v0.9.7 ke liye sahi imports
from pytgcalls import StreamType 
from core.call import call_py
from core.queues import get, is_empty, pop

async def start_stream(chat_id, file_path):
    try:
        # v0.9.7 mein AudioPiped ko bina kisi extra argument ke call karein
        # Agar URL extract ho rahi hai toh ye sahi format hai
        await call_py.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(
                    file_path,
                )
            ),
            stream_type=StreamType.pulse_stream 
        )
    except Exception as e:
        # Agar Assistant already join hai toh stream change karein
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
        # Check karein ki url ya file mil raha hai
        file_to_stream = next_track.get("url") or next_track.get("file")
        await start_stream(chat_id, file_to_stream)
