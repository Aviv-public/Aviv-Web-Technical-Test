from typing import Tuple

from flask import Flask, Response, jsonify, request
from werkzeug.exceptions import NotFound

from pricemap import registry
from pricemap.domain.entities.listings import ListingEntity
from pricemap.domain.exceptions.listings import ListingNotFoundException


app = Flask(__name__)


@app.route("/listings", methods=["GET"])
def get_listings() -> Tuple[Response, int]:
    """Get all listings."""
    listings_data = registry.retrieve_listings.perform()
    return jsonify(listings_data), 200


@app.route("/listings", methods=["POST"])
def post_listing() -> Tuple[Response, int]:
    """Create a listing."""
    data = request.get_json()
    listing = ListingEntity.parse_obj(data)
    listing_data = registry.persist_listing.perform(listing)
    return jsonify(listing_data), 201


@app.route("/listings/<int:id_>", methods=["PUT"])
def put_listing(id_: int) -> Tuple[Response, int]:
    """Update a listing."""
    data = request.get_json()
    listing = ListingEntity.parse_obj(data)
    try:
        listing_data = registry.update_listing.perform(id_, listing)
    except ListingNotFoundException:
        raise NotFound
    return jsonify(listing_data), 200


@app.route("/listings/<int:id_>/prices", methods=["GET"])
def get_price_history(id_: int) -> Tuple[Response, int]:
    """Get price history."""
    # TODO: implement this
    mock_response = [
        {"price_eur": 100000, "created_date": "2023-01-12T09:23:36Z"},
        {"price_eur": 150000, "created_date": "2023-01-17T08:17:32Z"},
    ]
    return jsonify(mock_response), 200
