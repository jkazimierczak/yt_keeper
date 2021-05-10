import youtube_dl

from . import CONFIG


ydl_opts = {
    'outtmpl': f'{CONFIG.output_to}/%(playlist)s/%(title)s-%(id)s.%(ext)s'
}


class Playlist:
    @staticmethod
    def download(urls: list[str]):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

    @staticmethod
    def keep():
        Playlist.download(CONFIG.playlists)
