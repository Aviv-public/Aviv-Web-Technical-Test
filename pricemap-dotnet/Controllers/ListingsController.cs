using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using pricemap.Infrastructure.Database;
using pricemap.Models;
using System;
using System.Collections.Generic;
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
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(ICollection<RealEstateListing>))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public IActionResult GetListingsAsync()
        {
            try
            {
                var r = new List<RealEstateListing>();
                var listings = _listingsContext.Listings.ToList();
                foreach (var listing in listings)
                {
                    var rel = new RealEstateListing
                    {
                        Id = listing.Id,
                        BedroomsCount = listing.BedroomsCount,
                        BuildingType = listing.BuildingType,
                        ContactPhoneNumber = listing.ContactPhoneNumber,
                        CreatedDate = listing.CreatedDate,
                        UpdatedDate = listing.UpdatedDate,
                        Name = listing.Name,
                        Description = listing.Description,
                        Price = new Price
                        {
                            Price_eur = listing.Price,
                            Date_posted = listing.PriceDatePosted
                        },
                        RoomsCount = listing.RoomsCount,
                        SurfaceAreaM2 = listing.SurfaceAreaM2,
                        PostalAddress = new PostalAddress
                        {
                            City = listing.City,
                            Country = listing.Country,
                            PostalCode = listing.PostalCode,
                            StreetAddress = listing.StreetAddress
                        }
                    };
                    r.Add(rel);
                }
                return Ok(r);
            }
            catch (Exception e)
            {
                _logger.LogError($"GetListingsAsync. Error : {e}");
                return StatusCode(500);
            }
        }

        /// <summary>
        /// Get listing price history
        /// </summary>
        /// <param name="id">The id for the listing to get price history from</param>
        /// <returns></returns>
        [HttpGet]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(ICollection<Price>))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        [Route("{id}/history")]
        public IActionResult GetListingPriceHistoryAsync(int id)
        {
            try
            {
                var prices = _listingsContext.Prices.Where(p => p.ListingId == id);
                return Ok(prices?.Select(p => new Price
                {
                    Date_posted = p.PriceDate,
                    Price_eur = p.PriceValue
                }));
            }
            catch (Exception e)
            {
                _logger.LogError($"GetListingPriceHistoryAsync. Id : {id}. Error : {e}");
                return StatusCode(500);
            }
        }

        [HttpPut]
        [ProducesResponseType(StatusCodes.Status200OK, Type = typeof(RealEstateListing))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public async Task<IActionResult> PutListingAsync(RealEstateListing listing, CancellationToken cancellationToken)
        {
            try
            {
                var r = _listingsContext.Listings.FirstOrDefault(l => l.Id == listing.Id);
                if (r == null) return NotFound();

                // Update listing
                r.BedroomsCount = listing.BedroomsCount;
                r.BuildingType = listing.BuildingType;
                r.ContactPhoneNumber = listing.ContactPhoneNumber;
                r.CreatedDate = listing.CreatedDate;
                r.UpdatedDate = listing.UpdatedDate;
                r.Name = listing.Name;
                r.Description = listing.Description;
                r.Price = listing.Price.Price_eur;
                r.PriceDatePosted = listing.Price.Date_posted;
                r.RoomsCount = listing.RoomsCount;
                r.SurfaceAreaM2 = listing.SurfaceAreaM2;
                r.City = listing.PostalAddress.City;
                r.Country = listing.PostalAddress.Country;
                r.PostalCode = listing.PostalAddress.PostalCode;
                r.StreetAddress = listing.PostalAddress.StreetAddress;
                _listingsContext.Listings.Update(r);
                _listingsContext.Prices.Add(new Infrastructure.Database.Models.Price()
                {
                    ListingId = listing.Id,
                    PriceValue = listing.Price.Price_eur,
                    PriceDate = listing.Price.Date_posted
                });
                await _listingsContext.SaveChangesAsync(cancellationToken).ConfigureAwait(false);
                return Ok(listing);

            }
            catch (Exception ex)
            {
                _logger.LogError($"PutListingAsync. Listing : {listing}. Exception : {ex}");
                return StatusCode(500);
            }
        }

        [HttpPost]
        [ProducesResponseType(StatusCodes.Status201Created, Type = typeof(RealEstateListing))]
        [ProducesResponseType(StatusCodes.Status500InternalServerError)]
        public async Task<IActionResult> PostListingAsync(RealEstateListing listing, CancellationToken cancellationToken)
        {
            try
            {
                var r = _listingsContext.Listings.FirstOrDefault(l => l.Id == listing.Id);
                if (r == null)
                {
                    // Insert
                    r = new Infrastructure.Database.Models.Listing
                    {
                        Id = listing.Id,
                        BedroomsCount = listing.BedroomsCount,
                        BuildingType = listing.BuildingType,
                        ContactPhoneNumber = listing.ContactPhoneNumber,
                        CreatedDate = listing.CreatedDate,
                        UpdatedDate = listing.UpdatedDate,
                        Name = listing.Name,
                        Description = listing.Description,
                        Price = listing.Price.Price_eur,
                        PriceDatePosted = listing.Price.Date_posted,
                        RoomsCount = listing.RoomsCount,
                        SurfaceAreaM2 = listing.SurfaceAreaM2,
                        City = listing.PostalAddress.City,
                        Country = listing.PostalAddress.Country,
                        PostalCode = listing.PostalAddress.PostalCode,
                        StreetAddress = listing.PostalAddress.StreetAddress
                    };
                    _listingsContext.Listings.Add(r);
                    _listingsContext.Prices.Add(new Infrastructure.Database.Models.Price()
                    {
                        ListingId = listing.Id,
                        PriceValue = listing.Price.Price_eur,
                        PriceDate = listing.Price.Date_posted
                    });
                    await _listingsContext.SaveChangesAsync(cancellationToken).ConfigureAwait(false);
                }
                return StatusCode(StatusCodes.Status201Created, listing);
            }
            catch (Exception ex)
            {
                _logger.LogError($"PostListingAsync. Listing : {listing}. Exception : {ex}");
                return StatusCode(500);
            }
        }
    }
}
