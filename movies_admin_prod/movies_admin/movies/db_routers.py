import logging

from .models import FilmWork, GenreFilmWork, Genre, Person, PersonFilmWork

ROUTED_MODELS = [FilmWork, GenreFilmWork, Genre, Person, PersonFilmWork]


# ** hints are  MUST have due to instance error
class FilmDBRouter:
    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            logging.error(hints)
            return 'movies'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            logging.error(hints)
            return 'movies'
        return None
