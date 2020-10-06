import json
import logging
import os
import collections
import sys
from io import BytesIO

import requests
import typing
from lxml import etree

logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


base_url = "https://www-staging.meilleursagents.org/annonces/achat/paris-75000/appartement/"


subcity_place_id = {
        "Paris 1er arrondissement": 32682,
        "Paris 2\u00e8me arrondissement": 32683,
        "Paris 3\u00e8me arrondissement": 32684,
        "Paris 4\u00e8me arrondissement": 32685,
        "Paris 5\u00e8me arrondissement": 32686,
        "Paris 6\u00e8me arrondissement": 32687,
        "Paris 7\u00e8me arrondissement": 32688,
        "Paris 8\u00e8me arrondissement": 32689,
        "Paris 9\u00e8me arrondissement": 32690,
        "Paris 10\u00e8me arrondissement": 32691,
        "Paris 11\u00e8me arrondissement": 32692,
        "Paris 12\u00e8me arrondissement": 32693,
        "Paris 13\u00e8me arrondissement": 32694,
        "Paris 14\u00e8me arrondissement": 32695,
        "Paris 15\u00e8me arrondissement": 32696,
        "Paris 16\u00e8me arrondissement": 32697,
        "Paris 17\u00e8me arrondissement": 32698,
        "Paris 18\u00e8me arrondissement": 32699,
        "Paris 19\u00e8me arrondissement": 32700,
        "Paris 20\u00e8me arrondissement": 32701,
}

ListingPageGenerator = typing.Generator[typing.Tuple[bytes, int], None, None]
ListingDataGenerator = typing.Generator[typing.Tuple[int, typing.Dict[str, str]], None, None]


def page_fetcher() -> ListingPageGenerator:
    page_number = 1
    while True:
        logger.info("Fetching page %d", page_number)

        response = requests.get(base_url + f"?page={page_number}")
        if response.status_code == 416:
            return
        if response.status_code != 200:
            logger.error("Enable to fetch page %d", page_number)
            yield b"", -1

        yield response.content, page_number

        page_number += 1


def disk_fetcher(directory: str) -> ListingPageGenerator:
    for path in os.listdir(path=directory):
        with open(os.path.join(directory, path), 'rb') as fd:
            page_number = int(os.path.splitext(path)[0])
            yield fd.read(), page_number


def parser(fetcher: ListingPageGenerator) -> ListingDataGenerator:
    for content, page_number in fetcher:
        logger.info("Parsing page %d", page_number)

        parser = etree.HTMLParser()
        tree = etree.parse(BytesIO(content), parser)
        listing = tree.xpath("//*[@data-search-listing-item]")
        data = [
                {
                    "title": item.xpath(".//*[@data-search-listing-item-title]")[0].text.strip(),
                    "price": item.xpath(".//*[@data-search-listing-item-price]")[0].text.strip(),
                    "place": item.xpath(".//*[@data-search-listing-item-place]")[0].text.strip(),
                    "listing_id": item.attrib["data-wa-data"].split("|")[0].split("=")[1]
                }
                for item in listing
        ]
        yield page_number, data


if __name__ == "__main__":
    result = collections.defaultdict(list)

    errors = 0
    for number, data in parser(page_fetcher()):
        for listing in data:
            try:
                result[subcity_place_id[listing["place"]]].append(listing)
            except Exception as exc:
                logger.exception("Error while indexing listing by place ID")
                errors += 1

    logger.info("Ignoring %d listings", errors)
    for place_id, listings in result.items():
        cwd = os.path.dirname(__file__)
        file_path = os.path.join(cwd, "listingapi", "storage", f"{place_id}.json")

        logger.info("Store place_id %d", place_id)
        with open(file_path, "w") as fd:
            fd.write(json.dumps(listings))
