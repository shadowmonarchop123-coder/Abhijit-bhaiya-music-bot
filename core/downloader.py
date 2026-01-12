import os
import yt_dlp
import uuid

def download_audio(url):
    os.makedirs("downloads", exist_ok=True)

    uid = str(uuid.uuid4())
    outtmpl = f"downloads/{uid}.%(ext)s"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "noplaylist": True,
        "quiet": True,
        "cookiefile": "cookies.txt",
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
        final_file = f"downloads/{uid}.mp3"

    return final_file, info
