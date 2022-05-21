import contextlib
import os
import sqlite3

import psycopg2
from dotenv import load_dotenv
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from sqlite_to_postgres.sql_postgres_migration import DB_Migration
load_dotenv("../.env")

TABLE_DATACLASS_NAME = {
    "film_work": "Film",
    "genre": "Genre",
    "person": "Person",
    "person_film_work": "PersonFilmWork",
    "genre_film_work": "GenreFilmWork",
}


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    migration = DB_Migration(connection_postgres=pg_conn, connection_sqlite=connection)
    for table_name, dataclass_name in TABLE_DATACLASS_NAME.items():
        migration.sql_postgres_batch_migration(
            table_name=table_name, dataclass_name=dataclass_name
        )


if __name__ == "__main__":
    dsl = {
        "dbname": os.environ.get("DB_NAME"),
        "user": os.environ.get("DB_USER"),
        "password": os.environ.get("DB_PASSWORD"),
        "host": "127.0.0.1",
        "port": 5432,
    }
    with contextlib.closing(
        sqlite3.connect("db.sqlite")
    ) as sqlite_conn, psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
