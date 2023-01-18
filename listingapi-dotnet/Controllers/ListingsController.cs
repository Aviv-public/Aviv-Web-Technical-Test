using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using listingapi.Infrastructure.Database;
using listingapi.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace listingapi.Controllers
{
    [Route("api/listings")]
    public class ListingsController : ControllerBase
    {
        #region Properties
        private readonly ListingsContext _listingsContext;
        private readonly ILogger<ListingsController> _logger;

        public ListingsController(ILogger<ListingsController> logger, ListingsContext listingsContext)
        {
            _logger = logger;
            _listingsContext = listingsContext;
        }
        #endregion

        /// <summary>
        /// Get all the listings registered in the app
        /// </summary>
        /// <param name="cog">cog the place</param>
        /// <returns></returns>
        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(ICollection<ListingReadOnly>))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult GetListingsAsync()
        {
            try
            {
                var results = new List<ListingReadOnly>();
                var listings = _listingsContext.Listings.ToList();
                foreach (var listing in listings)
                {
                    results.Add(MapListing(listing));
                }
                return Ok(results);
            }
            catch (Exception e)
            {
                _logger.LogError($"GetListingsAsync. Error : {e}");
                return StatusCode(500);
            }
        }
        /// <summary>
        /// Create a listing
        /// </summary>
        /// <param name="listing"></param>
        /// <param name="cancellationToken"></param>
        /// <returns></returns>
        [HttpPost]
        [ProducesResponseType(StatusCodes.Status201Created, Type = typeof(ListingReadOnly))]
        [ProducesResponseType(StatusCodes.Status422UnprocessableEntity)]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public async Task<IActionResult> PostListingAsync([FromBody] Listing listing, CancellationToken cancellationToken)
        {
            if (listing == null || listing.PostalAddress == null)
                return BadRequest();
            try
            {
                // Insert
                var createDate = DateTime.Now;
                var result = new Infrastructure.Database.Models.Listing
                {
                    BedroomsCount = listing.BedroomsCount,
                    BuildingType = listing.BuildingType.ToString(),
                    ContactPhoneNumber = listing.ContactPhoneNumber,
                    CreatedDate = createDate,
                    UpdatedDate = createDate,
                    Name = listing.Name,
                    Description = listing.Description,
                    Price = listing.LatestPriceEur,
                    PriceDatePosted = createDate,
                    RoomsCount = listing.RoomsCount,
                    SurfaceAreaM2 = listing.SurfaceAreaM2,
                    City = listing.PostalAddress.City,
                    Country = listing.PostalAddress.Country,
                    PostalCode = listing.PostalAddress.PostalCode,
                    StreetAddress = listing.PostalAddress.StreetAddress,
                };
                _listingsContext.Listings.Add(result);
                await _listingsContext.SaveChangesAsync(cancellationToken).ConfigureAwait(false);

                return StatusCode(StatusCodes.Status201Created, MapListing(result));
            }
            catch (Exception ex)
            {
                _logger.LogError($"PostListingAsync. Listing : {listing}. Exception : {ex}");
                return StatusCode(500);
            }
        }

        /// <summary>
        /// Update a listing
        /// </summary>
        /// <param name="listing"></param>
        /// <param name="cancellationToken"></param>
        /// <returns></returns>
        [HttpPut]
        [Route("{id}")]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(ListingReadOnly))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public async Task<IActionResult> PutListingAsync(int id, [FromBody] Listing listing, CancellationToken cancellationToken)
        {
            if (id <= 0 || listing == null || listing.PostalAddress == null)
                return BadRequest();

            try
            {
                // include Prices here
                var result = _listingsContext.Listings
                    .FirstOrDefault(l => l.Id == id);
                if (result == null) return NotFound();

                // Update listing
                var priceDate = DateTime.Now;
                result.BedroomsCount = listing.BedroomsCount;
                result.BuildingType = listing.BuildingType.ToString();
                result.ContactPhoneNumber = listing.ContactPhoneNumber;
                result.UpdatedDate = DateTime.Now;
                result.Name = listing.Name;
                result.Description = listing.Description;
                result.Price = listing.LatestPriceEur;
                result.PriceDatePosted = priceDate;
                result.RoomsCount = listing.RoomsCount;
                result.SurfaceAreaM2 = listing.SurfaceAreaM2;
                result.City = listing.PostalAddress.City;
                result.Country = listing.PostalAddress.Country;
                result.PostalCode = listing.PostalAddress.PostalCode;
                result.StreetAddress = listing.PostalAddress.StreetAddress;
                _listingsContext.Listings.Update(result);
                await _listingsContext.SaveChangesAsync(cancellationToken).ConfigureAwait(false);
                return Ok(MapListing(result));
            }
            catch (Exception ex)
            {
                _logger.LogError($"PutListingAsync. Listing : {listing}. Exception : {ex}");
                return StatusCode(500);
            }
        }

        /// <summary>
        /// Get listing price history
        /// </summary>
        /// <param name="id">The id for the listing to get price history from</param>
        /// <returns></returns>
        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(ICollection<PriceReadOnly>))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [Route("{id}/history")]
        public IActionResult GetListingPriceHistory(int id)
        {
            // ToDo : implement me !
            return Ok(new List<PriceReadOnly>
            {
                new PriceReadOnly
                {
                    PriceEur = 130000
                },
                new PriceReadOnly
                {
                    PriceEur = 250000
                }
            });
        }

        private static ListingReadOnly MapListing(Infrastructure.Database.Models.Listing listing)
        {
            return new ListingReadOnly
            {
                Id = listing.Id,
                CreatedDate = listing.CreatedDate,
                UpdatedDate = listing.UpdatedDate,
                Price = new PriceReadOnly
                {
                    PriceEur = listing.Price,
                    CreatedDate = listing.PriceDatePosted
                },
                BedroomsCount = listing.BedroomsCount,
                BuildingType = listing.BuildingType,
                ContactPhoneNumber = listing.ContactPhoneNumber,
                Description = listing.Description,
                Name = listing.Name,
                PostalAddress = new PostalAddress
                {
                    City = listing.City,
                    Country = listing.Country,
                    PostalCode = listing.PostalCode,
                    StreetAddress = listing.StreetAddress
                },
                RoomsCount = listing.RoomsCount,
                SurfaceAreaM2 = listing.SurfaceAreaM2
            };
        }
    }
}
