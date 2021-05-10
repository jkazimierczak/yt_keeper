import youtube_dl

from . import RELATIVE_ROOT


ydl_opts = {
    'outtmpl': f'{RELATIVE_ROOT}/downloads/%(playlist)s/%(title)s-%(id)s.%(ext)s'
}


class Playlist:
    @staticmethod
    def download(urls: list[str]):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)

    @staticmethod
    def keep():
        Playlist.download([
            'https://www.youtube.com/playlist?list=PLD954AD90548599FE'
        ])
