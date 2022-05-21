from sqlite_to_postgres.data_validation_classes import (
    Film,
    Genre,
    GenreFilmWork,
    Person,
    PersonFilmWork,
)


class DataValidation:
    def __init__(self):
        self.validated_data = []

    def validate_loaded_batch(self, loaded_data: list, dataclass_name: str):
        if dataclass_name == "Film":
            for item in loaded_data:
                table_row = {k: item[k] for k in item.keys()}
                film = Film(
                    id=table_row["id"],
                    title=table_row["title"],
                    description=table_row["description"],
                    creation_date=table_row["creation_date"],
                    certificate=table_row["certificate"],
                    file_path=table_row["file_path"],
                    rating=table_row["rating"],
                    type=table_row["type"],
                    created_at=table_row["created_at"],
                )
                self.validated_data.append(
                    (
                        film.id,
                        film.title,
                        film.description,
                        film.creation_date,
                        film.certificate,
                        film.file_path,
                        film.rating,
                        film.type,
                        film.created_at,
                        film.updated_at,
                    )
                )
            return self.validated_data

        if dataclass_name == "Genre":
            for item in loaded_data:
                table_row = {k: item[k] for k in item.keys()}
                genre = Genre(
                    id=table_row["id"],
                    name=table_row["name"],
                    description=table_row["description"],
                    created_at=table_row["created_at"],
                )
                self.validated_data.append(
                    (
                        genre.id,
                        genre.name,
                        genre.description,
                        genre.created_at,
                        genre.updated_at,
                    )
                )
            return self.validated_data

        if dataclass_name == "GenreFilmWork":
            for item in loaded_data:
                table_row = {k: item[k] for k in item.keys()}
                genre_film_work = GenreFilmWork(
                    id=table_row["id"],
                    film_work_id=table_row["film_work_id"],
                    genre_id=table_row["genre_id"],
                    created_at=table_row["created_at"],
                )
                self.validated_data.append(
                    (
                        genre_film_work.id,
                        genre_film_work.film_work_id,
                        genre_film_work.genre_id,
                        genre_film_work.created_at,
                    )
                )
            return self.validated_data
        if dataclass_name == "Person":
            for item in loaded_data:
                table_row = {k: item[k] for k in item.keys()}
                person = Person(
                    id=table_row["id"],
                    full_name=table_row["full_name"],
                    birth_date=table_row["birth_date"],
                    created_at=table_row["created_at"],
                )
                self.validated_data.append(
                    (
                        person.id,
                        person.full_name,
                        person.birth_date,
                        person.created_at,
                        person.updated_at,
                    )
                )
            return self.validated_data
        if dataclass_name == "PersonFilmWork":
            for item in loaded_data:
                table_row = {k: item[k] for k in item.keys()}
                person_film_work = PersonFilmWork(
                    id=table_row["id"],
                    film_work_id=table_row["film_work_id"],
                    person_id=table_row["person_id"],
                    role=table_row["role"],
                )
                self.validated_data.append(
                    (
                        person_film_work.id,
                        person_film_work.film_work_id,
                        person_film_work.person_id,
                        person_film_work.role,
                        person_film_work.created_at,
                    )
                )
            return self.validated_data
