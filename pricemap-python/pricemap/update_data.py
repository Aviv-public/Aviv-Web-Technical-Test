from datetime import datetime

import requests

from pricemap import db_pool

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


def init_database() -> None:
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
    connection = db_pool.getconn()
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception:
        connection.rollback()
        print("Error: maybe table already exists?")
    finally:
        cursor.close()
        db_pool.putconn(connection)  # re-put connection to db pool
    return


def update() -> None:
    # init database
    init_database()
    connection = db_pool.getconn()
    cursor = connection.cursor()
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

                room_count = __extract_rooms(item["title"])
                area = __extract_area(item["title"])
                price = __extract_price(item["price"])

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
                try:
                    cursor.execute(sql)
                    cursor.commit()
                finally:
                    cursor.close()
                    db_pool.putconn(connection)  # re-put connection to db pool


def __extract_area(title: str) -> int:
    try:
        area = int(title.split("-")[1].replace(" ", "").replace("\u00a0m\u00b2", ""))
    except Exception:
        area = 0
    return area


def __extract_price(price_str: str) -> int:
    try:
        price = int("".join([s for s in price_str if s.isdigit()]))
    except Exception:
        price = 0
    return price


def __extract_rooms(title: str) -> int:
    try:
        room_count = (
            1
            if "Studio" in title
            else int("".join([s for s in title.split("pièces")[0] if s.isdigit()]))
        )
    except Exception:
        room_count = 0
    return room_count
