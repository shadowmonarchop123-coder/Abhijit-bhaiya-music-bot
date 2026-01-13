import asyncio
import traceback # Error ki poori detail nikalne ke liye
from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls.types import StreamType 
from core.call import call_py
from core.queues import get, is_empty
from config import FFMPEG_COMMAND

async def start_stream(chat_id, file_path):
    try:
        # Pehle join karne ki koshish
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
    except Exception as e:
        # Agar join fail hota hai toh terminal mein error print hoga
        print(f"❌ Join Error: {e}")
        
        try:
            # Join fail hone par stream change try karein
            await call_py.change_stream(
                chat_id,
                InputStream(
                    AudioPiped(
                        file_path,
                        ffmpeg_parameters=FFMPEG_COMMAND 
                    )
                )
            )
        except Exception as ex:
            # Agar change stream bhi fail ho jaye
            print(f"❌ Change Stream Error: {ex}")
            traceback.print_exc() # Yeh poora error report dikhayega

async def play_next(chat_id):
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except Exception:
            pass
        return

    next_track = get(chat_id)
    file_to_stream = next_track.get("url") or next_track.get("file")
    
    if not file_to_stream:
        print("❌ No file or URL found to stream!")
        return

    try:
        await start_stream(chat_id, file_to_stream)
    except Exception as e:
        print(f"❌ Play Next Error: {e}")
        traceback.print_exc()
