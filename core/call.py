from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.stream import StreamAudioEnded

from core.client import user
from core.queues import pop, is_empty
# Yahan se plugins.play hata diya gaya hai loop todne ke liye

call_py = PyTgCalls(user)


@call_py.on_stream_end()
async def on_stream_end(_: PyTgCalls, update: Update):
    # LOCAL IMPORT: Jab gaana khatam hoga, tabhi ye play_next ko bulayega
    from plugins.play import play_next
    
    chat_id = update.chat_id

    # Queue se khatam hua gaana nikalein
    pop(chat_id)

    if not is_empty(chat_id):
        # Agar queue mein aur gaane hain, to agla bajayein
        await play_next(chat_id)
    else:
        # Agar queue khali hai, to VC chhod dein
        try:
            await call_py.leave_group_call(chat_id)
        except Exception:
            pass
