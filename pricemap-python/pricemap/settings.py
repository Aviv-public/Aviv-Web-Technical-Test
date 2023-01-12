# -*- coding: utf-8 -*-

# Service
import os


# Database
DATABASE = {
    "database": os.getenv("PGDATABASE"),
    "user": os.getenv("PGUSER"),
    "password": os.getenv("PGPASSWORD"),
    "host": "db",
    "port": 5432,
}

LISTING_API_URI = "http://listingapi:5000/listings/%d"
LISTING_API_NB_RESULTS_PER_PAGE = 20
