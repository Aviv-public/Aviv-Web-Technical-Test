import os
import json

from flask import Flask, request, jsonify, make_response
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)


@app.route("/listings/<int:place_id>", methods=["GET"])
def listings(place_id: int):
    query_params = dict(request.args)
    try:
        page = int(query_params.get("page", 1))
    except ValueError:
        raise BadRequest(f"\"page\" should be an integer, given value: {page}!")

    cwd = os.path.dirname(__file__)
    file_path = os.path.join(cwd, "storage", f"{place_id}.json")
    if not os.path.exists(file_path):
        raise NotFound(f"\"place_id\" {place_id} not found!")

    with open(file_path) as fd:
        listings = json.load(fd)

    page_size = 20
    offset = page * page_size
    if offset >= len(listings):
        return make_response("", 416)

    return jsonify(listings[offset:offset+page_size])
