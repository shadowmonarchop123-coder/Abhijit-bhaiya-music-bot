import os
import yt_dlp
import uuid

def download_audio(url):
    os.makedirs("downloads", exist_ok=True)
    filename = f"downloads/{uuid.uuid4()}.mp3"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": filename,
        "noplaylist": True,
        "quiet": True,
        "cookiefile": "cookies.txt",   # ✅ IMPORTANT
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    return filename, info
