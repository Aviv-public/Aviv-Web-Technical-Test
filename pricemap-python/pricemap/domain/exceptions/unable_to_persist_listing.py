from pricemap.domain.entities.listing import Listing


class UnableToPersistListing(Exception):
    """
    Raised when we try to persist a Listing but something wrong happens.

    Attributes:
        - listing - Listing entity that can't be persisted
    """

    def __init__(self, listing:Listing, previous_exception_message=""):
        self.listing = listing
        message = f"Unable to persist listing entity : {previous_exception_message}"
        super().__init__(message)
