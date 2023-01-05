"""Handles database sessions and connections."""

from psycopg2 import extras, pool

import settings

db_pool = pool.ThreadedConnectionPool(
    1, 20, **settings.DATABASE, cursor_factory=extras.DictCursor
)
