from flask import g, current_app
import requests
import psycopg2
from datetime import datetime

GEOMS_IDS = [
    32684,
    32683,
    32682,
    32685,
    32686,
    32687,
    32688,
    32689,
    32690,
    32691,
    32692,
    32693,
    32699,
    32694,
    32695,
    32696,
    32697,
    32698,
    32700,
    32701,
]

def init_database():
    sql = """
        CREATE TABLE listings (
            id INTEGER,
            place_id INTEGER,
            price INTEGER,
            area INTEGER,
            room_count INTEGER,
            seen_at TIMESTAMP,
            PRIMARY KEY (id, seen_at)
        );
    """
    cursor = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cursor.execute(sql)
        g.db.commit()
    except:
        g.db.rollback()
        print("Error: maybe table already exists?")
        return

def update():
    # init database
    init_database()
    db_cursor = g.db.cursor(cursor_factory=psycopg2.extras.DictCursor)

    for geom in GEOMS_IDS:
        p = 0
        while True:
            p += 1
            url = "http://listingapi:5000/listings/" + str(geom) + "?page=" + str(p)
            d = requests.get(url)

            # Break when finished
            if d.status_code == 416:
                break

            for item in d.json():
                listing_id = item["listing_id"]
                try:
                    room_count = 1 if "Studio" in item["title"] else int("".join([s for s in item["title"].split("pièces")[0] if s.isdigit()]))
                except:
                    room_count = 0

                try:
                    price =  int("".join([s for s in item["price"] if s.isdigit()]))
                except:
                    price = 0

                try:
                    area = int(item["title"].split("-")[1].replace(" ", '').replace("\u00a0m\u00b2", ''))
                except:
                    area = 0

                seen_at = datetime.now()

                sql = f"""
                    INSERT INTO listings VALUES(
                        {listing_id},
                        {geom},
                        {price},
                        {area},
                        {room_count},
                        '{seen_at}'
                    );
                """
                db_cursor.execute(sql)
                g.db.commit()