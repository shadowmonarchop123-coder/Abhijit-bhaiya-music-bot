from pytgcalls.types.input_stream import InputStream, AudioPiped
from pytgcalls import StreamType
from core.call import call_py
from core.queues import get, pop, is_empty
from core.prefetch import get_prefetch


async def start_stream(chat_id, url):
    try:
        await call_py.join_group_call(
            chat_id,
            InputStream(AudioPiped(url)),
            stream_type=StreamType().pulse_stream
        )
    except:
        await call_py.change_stream(
            chat_id,
            InputStream(AudioPiped(url))
        )


async def play_next(chat_id):
    if is_empty(chat_id):
        try:
            await call_py.leave_group_call(chat_id)
        except:
            pass
        return

    song = get(chat_id)

    prefetched = get_prefetch(chat_id)
    if prefetched:
        song = prefetched

    await start_stream(chat_id, song["url"])
