from flask import jsonify, request, Flask
from werkzeug.exceptions import NotFound

from domain.entities.listings import Listing as ListingModel
import registry
from domain.exceptions.listings import ListingNotFoundException


app = Flask(__name__)


@app.route("/api/listings", methods=["GET"])
def get_listings():
    """
    Get all listings.
    """
    listings_data = registry.retrieve_listings.perform()
    return jsonify(listings_data), 200


@app.route("/api/listings", methods=["POST"])
def post_listing():
    """
    Create a listing.
    """
    data = request.get_json()
    listing = ListingModel.parse_obj(data)
    listing_data = registry.persist_listing.perform(listing)
    return jsonify(listing_data), 201


@app.route("/api/listings/<int:id_>", methods=["PUT"])
def put_listing(id_: int):
    """
    Update a listing.
    """
    data = request.get_json()
    listing = ListingModel.parse_obj(data)
    try:
        listing_data = registry.update_listing.perform(id_, listing)
    except ListingNotFoundException:
        raise NotFound
    return jsonify(listing_data), 200
