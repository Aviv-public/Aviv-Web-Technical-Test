from flask import Flask, render_template

from pricemap.blueprints.api import api

app = Flask(__name__)
app.config.from_object("settings")
app.register_blueprint(api, url_prefix="/api")


@app.route("/")
def index() -> str:
    return render_template("index.html")
