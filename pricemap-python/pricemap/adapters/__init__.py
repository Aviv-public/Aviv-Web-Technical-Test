from psycopg2 import extras, pool

from pricemap import settings


db_pool = pool.ThreadedConnectionPool(
    1, 20, **settings.DATABASE, cursor_factory=extras.DictCursor
)
