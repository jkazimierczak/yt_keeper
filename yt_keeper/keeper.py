import youtube_dl

from . import CONFIG


ydl_opts = {
    'outtmpl': f'{CONFIG.output_to}/{CONFIG.output_template}'
}


class Keeper:
    @staticmethod
    def keep_all():
        """Download all videos from playlists present in config."""
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(CONFIG.playlists)
