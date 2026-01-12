import os

# ========== BOT CONFIG ==========
API_ID = int(os.getenv("API_ID", "22834593"))
API_HASH = os.getenv("API_HASH", "f400bc1d1baeb9ae93014ce3ee5ea835")
BOT_TOKEN = os.getenv("BOT_TOKEN", "6666555316:AAEBEexXKkXy_l9eO414wGXYa4p907EXTPc")
STRING_SESSION = os.getenv("STRING_SESSION", "BQFcbaEAj5NxCIU8FfUh9yTyJRus2cfcOENDLt3S5cBzU3GRdgEqu0aJsF830bwGDESnbk_9PHKwEDs8YQRvhbmvdxC71xZhJ34915RUl40FZkR3jhneWNkUEw_JAg0j_IMQb0tL3AtQme9Cn5jSFS5ixsJf_AMaGGkG8akwX69OJYO3-sgfxvKPT31aidz2OlS7IPTq842EdoioQTka8mxsLVgr8e7IrbZVMN-TJ5oPrEGrK8qfoLxlOjjO96IOoxDQOkUQ3zVUkArr02jB3CYPeZeB8zQqaS0xg3n-E2rq6VgeSEdlGOXIm29hhM_xk3wASEd69HIk9YU2TLofnzRR7hBxXwAAAAF5c5ovAA")

BOT_NAME = "AO Music Bot"

# ========== SETTINGS ==========
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "0"))

DOWNLOAD_DIR = "downloads"
MAX_QUEUE = 20
AUTO_LEAVE = True

# ========== STREAM ==========
FFMPEG_COMMAND = [
    "ffmpeg",
    "-reconnect", "1",
    "-reconnect_streamed", "1",
    "-reconnect_delay_max", "5",
    "-i", "{input}",
    "-f", "s16le",
    "-ac", "2",
    "-ar", "48000",
    "pipe:1"
]
