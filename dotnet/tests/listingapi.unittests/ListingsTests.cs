using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using Moq;
using listingapi.Controllers;
using listingapi.Infrastructure.Database;
using listingapi.Models;
using System.Text.RegularExpressions;
using Xunit;

namespace listingapi.unittests
{
    public class ListingsTests
    {
        private ListingsController _listingsController;
        public ListingsTests()
        {
            var loggerMock = new Mock<ILogger<ListingsController>>();

            var options = new DbContextOptionsBuilder<ListingsContext>().Options;
            var listingContextMock = new Mock<ListingsContext>(options);
            listingContextMock.Setup(m => m.Listings).Returns(new Mock<DbSet<Infrastructure.Database.Models.Listing>>().Object);
            _listingsController = new ListingsController(loggerMock.Object, listingContextMock.Object);
        }

        [Fact]
        public async Task TestCreateListingValid()
        {
            var listing = new Listing
            {
                Name = "Name",
                BedroomsCount = 3,
                BuildingType = RealEstateListingBuildingType.HOUSE,
                ContactPhoneNumber = "0751272285",
                Description = "Description",
                PostalAddress = new PostalAddress
                {
                    City = "City",
                    Country = "FR",
                    PostalCode = "13007",
                    StreetAddress = "47 quai de rive neuve"
                },
                LatestPriceEur = 130000,
                RoomsCount = 4,
                SurfaceAreaM2 = 87
            };
            var actionResult = await _listingsController.PostListingAsync(listing, new CancellationToken()) as ObjectResult;
            Assert.NotNull(actionResult);
        }

        [Fact]
        public async Task TesttCreateListingBadRequest()
        {
            var listing = new Listing
            {
                Name = "Name",
                BedroomsCount = 3,
                BuildingType = RealEstateListingBuildingType.HOUSE,
                ContactPhoneNumber = "0751272285",
                Description = "Description",
                RoomsCount = 4,
                SurfaceAreaM2 = 87
            };
            var actionResult = await _listingsController.PostListingAsync(listing, new CancellationToken()) as BadRequestResult;
            Assert.NotNull(actionResult);
        }

        [Fact]
        public async Task TestUpdatetListingBadRequest()
        {
            var listing = new Listing
            {
                Name = "Name",
                BedroomsCount = 3,
                BuildingType = RealEstateListingBuildingType.HOUSE,
                ContactPhoneNumber = "0751272285",
                Description = "Description",
                RoomsCount = 4,
                SurfaceAreaM2 = 87
            };
            var actionResult = await _listingsController.PutListingAsync(0, listing, new CancellationToken()) as BadRequestResult;
            Assert.NotNull(actionResult);
        }

        [Fact]
        public async Task TestGetListingPriceHistoryValid()
        {
            var actionResult = _listingsController.GetListingPriceHistory(0) as ObjectResult;
            Assert.NotNull(actionResult);
        }

        [Fact]
        public void TestPhoneNumberValid()
        {
            var contactPhoneNumber = "+33751272285";
            var regex = new Regex("^\\+[1-9]\\d{1,14}$");
            var result = regex.IsMatch(contactPhoneNumber);
            Assert.True(result);
        }

        [Fact]
        public void TestPostalCodeValid()
        {
            var postalCode = "13007";
            Assert.True(postalCode.Length == 5);
        }
    }
}
