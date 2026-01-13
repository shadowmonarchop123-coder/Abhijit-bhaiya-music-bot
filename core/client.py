from pyrogram import Client
from pyrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

# Bot Client: Isme workers badhane se commands fast execute hongi
app = Client(
    "AO_Music_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML,
    in_memory=True,
    workers=40 # 🔥 Fast response ke liye workers add kiye
)

# User Assistant: Isme workers badhane se streaming connection fast hoga
user = Client(
    "AO_User",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    in_memory=True,
    workers=20 # Assistant multitasking ke liye
)
