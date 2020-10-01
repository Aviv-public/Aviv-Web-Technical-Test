import json
import os
import collections
from io import BytesIO

import requests
from lxml import etree


base_url = "https://www-staging.meilleursagents.org/annonces/achat/paris-75000/"


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


def page_fetcher():
    page_number = 1
    while True:
        response = requests.get(base_url + f"?page={page_number}")
        if response.status_code == 416:
            return
        yield response.content, page_number
        page_number += 1


def disk_fetcher(directory):
    for path in os.listdir(path=directory):
        with open(os.path.join(directory, path), 'rb') as fd:
            page_number = int(os.path.splitext(path)[0])
            yield fd.read(), page_number


def parser(fetcher):
    for content, page_number in fetcher:
        parser = etree.HTMLParser()
        tree = etree.parse(BytesIO(content), parser)
        listing = tree.xpath("//*[@data-search-listing-item-characteristics]")
        data = [
                {
                    "title": item.xpath("./*[@data-search-listing-item-title]")[0].text.strip(),
                    "price": item.xpath("./*[@data-search-listing-item-price]")[0].text.strip(),
                    "place": item.xpath("./*[@data-search-listing-item-place]")[0].text.strip(),
                }
                for item in listing
        ]
        yield page_number, data


if __name__ == "__main__":
    # for response, page_number in get_pages():
    #     print(page_number)
    #     with open(f"{page_number}.html", "wb") as result_file:
    #         result_file.write(response.content)
    result = collections.defaultdict(list)
    error = 0
    for number, data in parser(disk_fetcher("html")):
        for listing in data:
            try:
                result[subcity_place_id[listing["place"]]].append(listing)
            except Exception as exc:
                error += 1

    print(error)
    for place_id, listings in result.items():
        # os.mkdir(os.path.join("json", str(place_id)))
        with open(f"json/{place_id}.json", "w") as fd:
            fd.write(json.dumps(listings))

