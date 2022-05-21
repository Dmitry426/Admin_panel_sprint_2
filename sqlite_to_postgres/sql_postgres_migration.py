import contextlib
import logging
from sqlite3 import Row

from psycopg2.extras import execute_batch

from sqlite_to_postgres.data_validation import DataValidation


class DB_Migration:
    def __init__(self, connection_postgres, connection_sqlite):
        self.conn_postgres = connection_postgres
        self.conn_sqlite = connection_sqlite
        self.query_select = None
        self.batch_size = 50
        self.queryset = {
            "Film": f"""
                         INSERT INTO content.film_work ( id, title, description ,creation_date
                         ,
                         certificate , file_path ,rating ,type , created_at, updated_at )
                         VALUES (%s, %s,%s, %s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING
                         """,
            "Genre": f"""
                         INSERT INTO content.genre ( id, name, description ,created_at ,
                         updated_at )
                         VALUES (%s, %s,%s, %s,%s) ON CONFLICT DO NOTHING
                         """,
            "Person": f"""
                         INSERT INTO content.person ( id, full_name, birth_date, created_at,
                         updated_at )
                         VALUES (%s, %s,%s, %s,%s) ON CONFLICT DO NOTHING
                         """,
            "PersonFilmWork": f"""
                         INSERT INTO content.person_film_work ( id, film_work_id , person_id ,
                         role , created_at)
                         VALUES (%s, %s,%s, %s,%s) ON CONFLICT DO NOTHING
                         """,
            "GenreFilmWork": f"""
                         INSERT INTO content.genre_film_work ( id,  film_work_id,
                         genre_id,created_at )
                         VALUES (%s, %s,%s, %s) ON CONFLICT DO NOTHING
                         """,
        }

    def sql_postgres_batch_migration(self, table_name: str, dataclass_name: str):
        self.query_select = f"SELECT * FROM {table_name} "
        try:
            with contextlib.closing(
                self.conn_sqlite.cursor(),
            ) as sql_cur, self.conn_postgres.cursor() as postgres_cur:
                sql_cur.row_factory = Row
                selected_all = sql_cur.execute(self.query_select)
                for data in iter(lambda: selected_all.fetchmany(self.batch_size), []):
                    self.conn_sqlite.commit()
                    validated = DataValidation().validate_loaded_batch(
                        loaded_data=data, dataclass_name=dataclass_name
                    )
                    self.save_batch(
                        data_to_load=validated,
                        dataclass_name=dataclass_name,
                        cursor=postgres_cur,
                    )
                    self.conn_postgres.commit()
        except Exception as e:
            logging.exception(e)

    def save_batch(self, data_to_load: list, dataclass_name: str, cursor):
        try:
            query = self.queryset[dataclass_name]
            execute_batch(cursor, query, data_to_load)
        except Exception as e:
            logging.exception(e)
