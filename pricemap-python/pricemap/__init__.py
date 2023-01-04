"""Handles database sessions and connections."""
import psycopg2
from psycopg2 import pool, extras
import settings

db_pool = psycopg2.pool.ThreadedConnectionPool(1,
                                               20,
                                               **settings.DATABASE,
                                               cursor_factory=psycopg2.extras.DictCursor
                                               )
