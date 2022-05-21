import logging

from .models import FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork

ROUTED_MODELS = [FilmWork, GenreFilmWork, Genre, Person, PersonFilmWork]


class FilmDBRouter:
    @staticmethod
    def db_for_read(model, **hints):
        if model in ROUTED_MODELS:
            logging.error(hints)
            return "movies"
        return None

    @staticmethod
    def db_for_write(model, **hints):
        if model in ROUTED_MODELS:
            logging.error(hints)
            return "movies"
        return None
