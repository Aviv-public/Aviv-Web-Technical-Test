from unittest.mock import patch, Mock

from pricemap.domain.finder.geo_place_finder import GeoPlaceFinder
from pricemap.domain.repository.listing_repository import ListingRepository
from pricemap.domain.usecases.import_all_listings import ImportAllListings


def mocked_requests_get(*args, **kwargs):
    """This method will be used by the mock to replace requests.get."""

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == "http://listingapi:5000/listings/1" and args[1] == {"page": 1}:
        return MockResponse(
            [
                {
                    "listing_id": "1969821243",
                    "place": "Paris 1er arrondissement",
                    "price": "102 000 €",
                    "title": "Studio - 6\u00a0m\u00b2",
                }
            ],
            200,
        )
    elif args[0] == "http://listingapi:5000/listings/2" and args[1] == {"page": 1}:
        return MockResponse(
            [
                {
                    "listing_id": "1969946393",
                    "place": "Paris 2ème arrondissement",
                    "price": "364\u202f000\u00a0\u20ac",
                    "title": "Appartement 2\u00a0pi\u00e8ces - 29\u00a0m\u00b2",
                }
            ],
            200,
        )
    elif args[0] == "http://listingapi:5000/listings/3" and args[1] == {"page": 1}:
        return MockResponse(
            [
                {
                    "listing_id": "1969341590",
                    "place": "Paris 3ème arrondissement",
                    "price": "Prix non communiqu\u00e9",
                    "title": "Appartement 3\u00a0pi\u00e8ces - 57\u00a0m\u00b2",
                },
                {
                    "listing_id": "1969341590",
                    "place": "Paris 3ème arrondissement",
                    "price": "639\u202f000\u00a0\u20ac",
                    "title": "Appartement 3\u00a0pi\u00e8ces",
                },
            ],
            200,
        )

    return MockResponse(None, 416)


class TestImportAllListings:
    @patch("requests.get", side_effect=mocked_requests_get)
    def test_it_imports_nothing_when_no_listings_are_found(self, request):
        geo_place_finder = Mock(spec=GeoPlaceFinder)
        geo_place_finder.retrieve_all_places.return_value = [42]
        listing_repository = Mock(spec=ListingRepository)
        sut = ImportAllListings("http://listingapi:5000/listings/%d")

        sut.import_all_listings()
        assert 0 == listing_repository.insert.call_count
        assert 0 == listing_repository.exists.call_count
        assert 0 == listing_repository.update.call_count

        # self.assertIn(mock.call('http://listingapi:5000/listings/42', {'page': 1}), request.call_args_list)

    # @patch('requests.get', side_effect=mocked_requests_get)
    # def test_it_imports_listings(self, request):
    #    clock = datetime.now()
    #    geo_place_finder = Mock(spec=GeoPlaceFinder)
    #    geo_place_finder.retrieve_all_places.return_value = [1, 2]
    #    listing_repository = Mock(spec=ListingRepositoryInterface)
    #    listing_repository.exists.return_value = False


#
#    sut = ImportListingsService(
#        'http://listingapi:5000/listings/%d',
#        geo_place_finder,
#        listing_repository,
#        clock
#    )
#
#    sut.import_all_listings()
#
#    self.assertEqual(2, listing_repository.exists.call_count)
#    listing_repository.exists.assert_has_calls([mock.call(1969821243), mock.call(1969946393)])
#    self.assertEqual(2, listing_repository.insert.call_count)
#    listing_repository.insert.assert_has_calls(
#        [
#            mock.call(Listing(1969821243, [ListingPriceHistory(1969821243, 102000, clock)], 1, 1, 6,
#                              "Studio - 6 m²")),
#            mock.call(Listing(1969946393, [ListingPriceHistory(1969946393, 364000, clock)], 2, 2, 29,
#                              "Appartement 2 pièces - 29 m²"))
#        ]
#    )
#    self.assertEqual(0, listing_repository.update.call_count)
#    self.assertIn(mock.call('http://listingapi:5000/listings/1', {'page': 1}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/1', {'page': 2}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/2', {'page': 1}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/2', {'page': 2}), request.call_args_list)
#
# @patch('requests.get', side_effect=mocked_requests_get)
# def test_it_updates_listings(self, request):
#    clock = datetime.now()
#    geo_place_finder = Mock(spec=GeoPlaceFinder)
#    geo_place_finder.retrieve_all_places.return_value = [1, 2]
#    listing_repository = Mock(spec=ListingRepositoryInterface)
#    listing_repository.exists.return_value = True
#
#    sut = ImportListingsService(
#        'http://listingapi:5000/listings/%d',
#        geo_place_finder,
#        listing_repository,
#        clock
#    )
#
#    sut.import_all_listings()
#
#    self.assertEqual(2, listing_repository.exists.call_count)
#    listing_repository.exists.assert_has_calls([mock.call(1969821243), mock.call(1969946393)])
#    self.assertEqual(0, listing_repository.insert.call_count)
#    self.assertEqual(2, listing_repository.update.call_count)
#    listing_repository.update.assert_has_calls(
#        [
#            mock.call(Listing(1969821243, [ListingPriceHistory(1969821243, 102000, clock)], 1, 1, 6,
#                              "Studio - 6 m²")),
#            mock.call(Listing(1969946393, [ListingPriceHistory(1969946393, 364000, clock)], 2, 2, 29,
#                              "Appartement 2 pièces - 29 m²"))
#        ]
#    )
#    self.assertIn(mock.call('http://listingapi:5000/listings/1', {'page': 1}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/1', {'page': 2}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/2', {'page': 1}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/2', {'page': 2}), request.call_args_list)
#
# @patch('requests.get', side_effect=mocked_requests_get)
# def test_it_ignores_listing_when_data_are_invalid(self, request):
#    clock = datetime.now()
#    geo_place_finder = Mock(spec=GeoPlaceFinder)
#    geo_place_finder.retrieve_all_places.return_value = [3]
#    listing_repository = Mock(spec=ListingRepositoryInterface)
#    listing_repository.exists.return_value = False
#
#    sut = ImportListingsService(
#        'http://listingapi:5000/listings/%d',
#        geo_place_finder,
#        listing_repository,
#        clock
#    )
#
#    sut.import_all_listings()
#
#    self.assertEqual(0, listing_repository.exists.call_count)
#    self.assertEqual(0, listing_repository.insert.call_count)
#    self.assertEqual(0, listing_repository.update.call_count)
#    self.assertIn(mock.call('http://listingapi:5000/listings/3', {'page': 1}), request.call_args_list)
#    self.assertIn(mock.call('http://listingapi:5000/listings/3', {'page': 2}), request.call_args_list)
#
