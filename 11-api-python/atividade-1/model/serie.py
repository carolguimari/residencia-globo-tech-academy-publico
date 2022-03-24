class SerieModel:
    _series_list = list()

    def __init__(self, title, synopsis, rate, image_URL, main_cast) -> None:
        self.id = round(time.time() * 1000)
        self.title = title
        self.synopsis = synopsis
        self.rate = rate
        self.image_URL = image_URLlist()
        self.main_cast = list()

    @classmethod
    def add_serie(cls, post):
        cls._posts_list.append(post)
