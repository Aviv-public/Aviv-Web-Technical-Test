import re


class ListingParser:
    NB_ROOMS_REGEX = re.compile(
        r"(?P<type>Appartement|Studio)( (?P<nb_rooms>\d+) pièces)?"
    )
    AREA_REGEX = re.compile(r"(?P<area>\d+) m²")

    @staticmethod
    def _handle_special_chars(title: str) -> str:
        return (
            title.replace("\u00a0", " ").replace("\u00e8", "è").replace("\u00b2", "²")
        )

    @classmethod
    def extract_nb_rooms_from_string(cls, title: str) -> int:
        """
        Parse title string to retrieve the number of rooms.

        Set default value to 0 if the title does not match the regex
        If the title contains 'Studio', that means 1 room
        If the title contains 'Appartement', we extract the number of rooms just after

        Examples :
            - Appartement 2 pièces - 29 m² -> 2
            - Studio - 6 m² -> 1
            - 12 m2 -> 0
            - Appartement - 29m2 -> 0

        Args:
            - title -- string that contains rooms data

        Returns:
            - rooms - The extracted rooms value from title
        """
        nb_rooms = 0

        regex_match = cls.NB_ROOMS_REGEX.search(cls._handle_special_chars(title))
        if regex_match:
            if regex_match.group("type") == "Studio":
                nb_rooms = 1
            elif regex_match.group("nb_rooms") is not None:
                nb_rooms = int(regex_match.group("nb_rooms"))
        return nb_rooms

    @classmethod
    def extract_area_from_string(cls, title: str) -> int:
        """
        Parse title string to retrieve area.

        Set default value to 0 if the title does not match the regex

        Examples :
            - Appartement 2 pièces - 29 m² -> 29
            - Studio - 6 m² -> 6
            - Appartement 3 pièces -> 0

        Args:
            - title -- string that contains area data

        Returns:
            - area - The extracted area value from title
        """
        area = 0

        regex_match = cls.AREA_REGEX.search(cls._handle_special_chars(title))

        if regex_match:
            area = int(regex_match.group("area"))

        return area

    @staticmethod
    def extract_price_from_string(price_str: str) -> int:
        """
        Parse price string to extract the integer value.

        Examples :
            - 1 670 000 € -> 1670000
            - Wrong value -> 0

        Args:
            - price_str -- un-formatted string that contains price

        Returns:
            - price - The formatted integer price
        """
        try:
            price = int("".join([s for s in price_str if s.isdigit()]))
        except Exception:
            price = 0

        return price
