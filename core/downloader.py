import os
import yt_dlp
from config import DOWNLOAD_DIR

ytdlp_opts = {
    "format": "bestaudio/best",
    "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",
    "quiet": True,
    "no_warnings": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192"
    }]
}

def download_audio(url):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    with yt_dlp.YoutubeDL(ytdlp_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)
        return file_path.replace(".webm", ".mp3").replace(".m4a", ".mp3"), info
