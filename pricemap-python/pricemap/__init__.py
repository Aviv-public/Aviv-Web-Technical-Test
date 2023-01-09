"""Handles database sessions and connections."""
import logging
import sys

from psycopg2 import extras, pool

import settings

db_pool = pool.ThreadedConnectionPool(
    1, 20, **settings.DATABASE, cursor_factory=extras.DictCursor
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
