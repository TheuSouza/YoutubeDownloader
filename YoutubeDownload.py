import yt_dlp

link = input('Link do vídeo para Download: ').strip()

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'video_download.%(ext)s',
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Finished downloading.')
except Exception as e:
    print(f"Erro durante o download: {e}")

