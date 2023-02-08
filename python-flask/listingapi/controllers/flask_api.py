from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import NotFound

from listingapi import registry
from listingapi.domain import entities
from listingapi.domain.entities import exceptions


app = Flask(__name__)
cors = CORS(app)


@app.route("/listings", methods=["GET"])
def get_listings() -> tuple[Response, int]:
    """Get all listings."""
    listings_data = registry.retrieve_listings_use_case.perform()
    return jsonify(listings_data), 200


@app.route("/listings", methods=["POST"])
def post_listing() -> tuple[Response, int]:
    """Create a listing."""
    data = request.get_json()
    listing = entities.ListingEntity.parse_obj(data)
    listing_data = registry.persist_listing_use_case.perform(listing)
    return jsonify(listing_data), 201


@app.route("/listings/<int:id_>", methods=["PUT"])
def put_listing(id_: int) -> tuple[Response, int]:
    """Update a listing."""
    data = request.get_json()
    listing = entities.ListingEntity.parse_obj(data)
    try:
        listing_data = registry.update_listing_use_case.perform(id_, listing)
    except exceptions.ListingNotFound:
        raise NotFound
    return jsonify(listing_data), 200


@app.route("/listings/<int:id_>/prices", methods=["GET"])
def get_price_history(id_: int) -> tuple[Response, int]:
    """Get price history."""
    # TODO: implement this
    mock_response = [
        {"price_eur": 100000, "created_date": "2023-01-12T09:23:36Z"},
        {"price_eur": 150000, "created_date": "2023-01-17T08:17:32Z"},
    ]
    return jsonify(mock_response), 200
