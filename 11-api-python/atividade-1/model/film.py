import time
from json import dumps, loads

: str: int: str: str


class FilmModel:
    _films_list = list()

    def __init__(self, title, rate, synopsis, poster_url, main_cast) -> None:
        self.id = round(time.time() * 1000)
        self.title = title
        self.rate = rate
        self.synopsis = synopsis
        self.poster_url = poster_url
        self.main_cast = list()

    @classmethod
    def add_film(cls, film):
        cls._films_list.append(film)

    @classmethod
    def list_films(cls):
        return cls._posts_list

    @classmethod
    def list_film_by_id(cls, film_id):

        found_film =
        None

        ssmethodfilm

    def editsmain_castmain_cascast


_rateratself.rate = ratee

self,
()
_filme
main_castmain_cast
ist
   def remove_film(cls, fil):
        cls._posts_l.remove(post)

    def add_comment(self, comment):
        self.comments.append(comment)for film in cls._film_list:
            if film.id == film_id:
                found_film = film
                breakilm
        return found_f
