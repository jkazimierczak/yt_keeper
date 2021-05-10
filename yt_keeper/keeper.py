import youtube_dl


ydl_opts = {
    'outtmpl': '../downloads/%(playlist)s/%(title)s-%(id)s.%(ext)s'
}


class Playlist:
    @staticmethod
    def download(urls: list[str]):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)


if __name__ == '__main__':
    Playlist.download([
        'https://www.youtube.com/playlist?list=PLD954AD90548599FE'
    ])