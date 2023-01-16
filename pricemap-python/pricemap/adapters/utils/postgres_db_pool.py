from contextlib import contextmanager
from typing import Iterator

from psycopg import Connection
from psycopg.rows import dict_row
from psycopg_pool import ConnectionPool

from pricemap import settings


class PostgresDbPool:

    __DB_POOL = None

    @classmethod
    def db_pool(cls) -> ConnectionPool:
        if cls.__DB_POOL is None:
            cls.__DB_POOL = ConnectionPool(
                conninfo=settings.DATABASE_CONNECTION_STRING,
                min_size=1,
                max_size=20,
                # By doing that, we pass the kwarg to the connect() function
                # https://www.psycopg.org/psycopg3/docs/api/pool.html#psycopg_pool.ConnectionPool
                kwargs={"row_factory": dict_row},
            )
        return cls.__DB_POOL

    @classmethod
    @contextmanager
    def get_connection(cls) -> Iterator[Connection]:
        conn = cls.db_pool().getconn()
        try:
            yield conn
        finally:
            cls.db_pool().putconn(conn)  # release the connection
