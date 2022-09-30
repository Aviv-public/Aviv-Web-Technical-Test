# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals

# Service
import os

# Database
DATABASE = {
    'database': os.getenv('PGDATABASE'),
    'user': os.getenv('PGUSER'),
    'password': os.getenv('PGPASSWORD'),
    'host': 'db',
    'port': 5432
}
