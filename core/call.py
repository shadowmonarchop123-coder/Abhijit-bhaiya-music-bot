from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from core.client import user #
from core.queues import pop, is_empty #

call_py = PyTgCalls(user)

@call_py.on_stream_end()
async def on_stream_end(_: PyTgCalls, update: Update):
    chat_id = update.chat_id
    pop(chat_id) #

    if not is_empty(chat_id): #
        # Circular import se bachne ke liye core.streamer use karein
        from core.streamer import play_next
        await play_next(chat_id)
    else:
        try:
            await call_py.leave_group_call(chat_id)
        except Exception:
            pass
