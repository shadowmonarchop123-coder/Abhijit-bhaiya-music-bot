from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.stream import StreamAudioEnded

from core.client import user
from core.queues import pop, is_empty
# Yahan se play_next ka import hata diya hai

call_py = PyTgCalls(user)


@call_py.on_stream_end()
async def on_stream_end(_: PyTgCalls, update: Update):
    # Local import loop break karne ke liye
    from plugins.play import play_next
    
    chat_id = update.chat_id

    pop(chat_id)

    if not is_empty(chat_id):
        await play_next(chat_id)
    else:
        try:
            await call_py.leave_group_call(chat_id)
        except Exception:
            pass
