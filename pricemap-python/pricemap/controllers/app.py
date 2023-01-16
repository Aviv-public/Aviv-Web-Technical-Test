from flask import Flask, Response, jsonify, render_template, request

from pricemap.blueprints.api import api
from pricemap.registry import persistListingUsecase


app = Flask(__name__)
app.config.from_object("pricemap.settings")
app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/listings", methods=["PUT"])
def persist_listing() -> Response:
    values = request.values
    persistListingUsecase.do(values)
    return jsonify(request.values)
