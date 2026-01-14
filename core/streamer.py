from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls import StreamType
from core.call import call_py
from core.queues import get, is_empty

async def start_stream(chat_id, url):
    stream = InputStream(
        AudioPiped(url)
    )

    try:
        await call_py.join_group_call(
            chat_id,
            stream,
            stream_type=StreamType().pulse_stream
        )
    except:
        await call_py.change_stream(chat_id, stream)


async def play_next(chat_id):
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        return

    song = get(chat_id)
    await start_stream(chat_id, song["url"])
