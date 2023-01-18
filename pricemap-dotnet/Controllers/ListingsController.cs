using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using NetTopologySuite.Simplify;
using pricemap.Infrastructure.Database;
using pricemap.Models;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace pricemap.Controllers
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
            if (listing == null || listing.PostalAddress == null || listing.Price == null) 
                return BadRequest();
            try
            {
                // Insert
                var priceDate = DateTime.Now;
                var result = new Infrastructure.Database.Models.Listing
                {
                    BedroomsCount = listing.BedroomsCount,
                    BuildingType = listing.BuildingType.ToString(),
                    ContactPhoneNumber = listing.ContactPhoneNumber,
                    CreatedDate = DateTime.Now,
                    UpdatedDate = DateTime.Now,
                    Name = listing.Name,
                    Description = listing.Description,
                    Price = listing.Price.LastPriceEur,
                    PriceDatePosted = priceDate,
                    RoomsCount = listing.RoomsCount,
                    SurfaceAreaM2 = listing.SurfaceAreaM2,
                    City = listing.PostalAddress.City,
                    Country = listing.PostalAddress.Country,
                    PostalCode = listing.PostalAddress.PostalCode,
                    StreetAddress = listing.PostalAddress.StreetAddress,
                    Prices = new List<Infrastructure.Database.Models.Price>
                    {
                       new Infrastructure.Database.Models.Price()
                        {
                            PriceValue = listing.Price.LastPriceEur,
                            PriceDate = priceDate
                        }
                    }
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
            if (id <= 0 || listing == null || listing.PostalAddress == null || listing.Price == null)
                return BadRequest();

            try
            {
                // include Prices here
                var result = _listingsContext.Listings
                    .Include(b => b.Prices)
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
                result.Price = listing.Price.LastPriceEur;
                result.PriceDatePosted = priceDate;
                result.RoomsCount = listing.RoomsCount;
                result.SurfaceAreaM2 = listing.SurfaceAreaM2;
                result.City = listing.PostalAddress.City;
                result.Country = listing.PostalAddress.Country;
                result.PostalCode = listing.PostalAddress.PostalCode;
                result.StreetAddress = listing.PostalAddress.StreetAddress;
                result.Prices.Add(new Infrastructure.Database.Models.Price()
                {
                    PriceValue = listing.Price.LastPriceEur,
                    PriceDate = DateTime.Now
                });
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
            if (id <= 0) return BadRequest();
            try
            {
                var prices = _listingsContext.Prices.Where(p => p.ListingId == id);
                return Ok(prices?.Select(p => new PriceReadOnly
                {
                    CreatedDate = p.PriceDate,
                    PriceEur = p.PriceValue
                }));
            }
            catch (Exception e)
            {
                _logger.LogError($"GetListingPriceHistoryAsync. Id : {id}. Error : {e}");
                return StatusCode(500);
            }
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
