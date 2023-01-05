from typing import Tuple

from flask import Flask, render_template

from pricemap.blueprints.api import api
from pricemap.update_data import update

app = Flask(__name__)
app.config.from_object("settings")
app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/update_data")
def update_data() -> Tuple[str, int]:
    """Update the data."""
    update()
    return "", 200
