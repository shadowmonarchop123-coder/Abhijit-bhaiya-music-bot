import asyncio
from pytgcalls.types.input_stream import InputStream, AudioPiped
# 🔥 VERSION 0.9.7 KE LIYE SAHI IMPORT YEH HAI:
from pytgcalls import StreamType 
from core.call import call_py
from core.queues import get, is_empty, pop
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    try:
        # v0.9.7 mein join_group_call aise likha jata hai
        await call_py.join_group_call(
            chat_id,
            InputStream(
                AudioPiped(
                    file_path,
                    ffmpeg_parameters=FFMPEG_COMMAND 
                )
            ),
            stream_type=StreamType.pulse_stream 
        )
    except Exception:
        # Agar Assistant pehle se call mein hai toh stream change karein
        try:
            await call_py.change_stream(
                chat_id,
                InputStream(
                    AudioPiped(
                        file_path,
                        ffmpeg_parameters=FFMPEG_COMMAND 
                    )
                )
            )
        except Exception as e:
            print(f"❌ Error in change_stream: {e}")

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
