# -*- coding: utf-8 -*-

# Service
import os


# Database
DATABASE = {
    "database": os.getenv("PGDATABASE"),
    "user": os.getenv("PGUSER"),
    "password": os.getenv("PGPASSWORD"),
    "host": os.getenv("PGHOST"),
    "port": 5432,
}
DATABASE_CONNECTION_STRING = (
    f"postgresql://"
    f'{DATABASE["user"]}:{DATABASE["password"]}'
    f'@{DATABASE["host"]}:{DATABASE["port"]}'
    f'/{DATABASE["database"]}'
)
