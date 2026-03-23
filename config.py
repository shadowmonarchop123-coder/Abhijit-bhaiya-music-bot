import os

# ========== BOT CONFIG ==========
API_ID = int(os.getenv("API_ID", "22834593"))
API_HASH = os.getenv("API_HASH", "f400bc1d1baeb9ae93014ce3ee5ea835")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8628889832:AAGl2wiVQiEwH1YMkFnc4R4Ys-sKUfHpK4k")
STRING_SESSION = os.getenv("STRING_SESSION", "1AZWarzgBu0-LXXerqIEwFt6o-Viu2gm9nEZ6XOLFDeuidQn9LD7iDtngA6916OD7HUFFrWl9HRqOK_5H0CzjJyYWhN8cKoWlr0atK_8rKMDbcE5zSfYJt75u1tqQeSayFxEvSxiDxGXnT5I-4ynojU5JNz3oKummAl1ugasDBuyYtwgbZdxxwWJlBQYa1AQrFZgL8_QteoOhRL4ncXNaYm4NkX-9-W3XVvO_7A50MbswGOkGh87zAOT00CKOrJVz-aiz196ckNCbRhpzc6oisOEHRdY9xXZPuQuA7w-PVcus4KT-pH3rzapQRfNKneYkv_EariXz4nTR-kbD5a7onkyRcAQTnoY=")

BOT_NAME = "✨Dᴀʀᴋ Aɴɢᴇʟ Music✨🤍"

# ========== SETTINGS ==========
OWNER_ID = int(os.getenv("OWNER_ID", "5390485406"))
# Yahan space hata dein "-100..." se pehle
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1003886464823"))

DOWNLOAD_DIR = "downloads"
MAX_QUEUE = 20
AUTO_LEAVE = True

# ========== STREAM (SUPER FAST CONFIG) ==========
# List ki jagah string format zyada stable hota hai kuch PyTgCalls versions mein
FFMPEG_COMMAND = (
    "-reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 "
    "-reconnect_delay_max 5 -i {input} "
    "-f s16le -ac 2 -ar 48000 -acodec pcm_s16le pipe:1"
)
