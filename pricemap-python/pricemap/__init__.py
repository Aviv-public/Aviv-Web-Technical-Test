"""Handles database sessions and connections."""
import logging
import sys

import psycopg2
import settings
from psycopg2 import pool, extras

db_pool = psycopg2.pool.ThreadedConnectionPool(1,
                                               20,
                                               **settings.DATABASE,
                                               cursor_factory=psycopg2.extras.DictCursor
                                               )

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
