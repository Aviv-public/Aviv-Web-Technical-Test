from pricemap import registry
from pricemap.controllers.listingapi import app
from factory import ListingFactory


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
