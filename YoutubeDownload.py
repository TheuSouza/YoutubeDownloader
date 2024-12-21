import yt_dlp

# solicita o link do vídeo.
link = input('Link do vídeo para Download: ').strip()

# Cria um dict com o melhor formato disponivel do video.
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': 'video_download.%(ext)s',
}

# Faz um Try para baixar o video, caso ocorra algum erro o mesmo é printado na tela.
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print('Finished downloading.')
except Exception as e:
    print(f"Erro durante o download: {e}")

