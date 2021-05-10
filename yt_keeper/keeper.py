import youtube_dl

from . import CONFIG


ydl_opts = {
    'outtmpl': f'{CONFIG.output_to}/%(playlist)s/%(title)s-%(id)s.%(ext)s'
}


class Keeper:
    @staticmethod
    def keep_all():
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(CONFIG.playlists)
