using pricemap.Services.Contracts;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using pricemap.Infrastructure.Database;
using System.Linq;
using pricemap.Services.Models;
using pricemap.Models;
using System.Text.RegularExpressions;

namespace pricemap.Controllers.V1
{
    [Route("api/v1")]
    public class PricemapController : ControllerBase
    {
        #region Properties
        private readonly PricemapContext _pricemapContext;
        private readonly IListingService _listingService;
        private readonly ILogger<PricemapController> _logger;

        public PricemapController(ILogger<PricemapController> logger, PricemapContext pricemapContext, IListingService listingService)
        {
            _logger = logger;
            _pricemapContext = pricemapContext;
            _listingService = listingService;
        }
        #endregion

        /// <summary>
        /// 
        /// </summary>
        /// <param name="cog">cog the place</param>
        /// <returns></returns>
        [HttpGet]
        [Route("get_price/{placeId}")]
        public async Task<IActionResult> GetPrice(string cog)
        {
            if (string.IsNullOrEmpty(cog)) return BadRequest();
            try
            {
                // ToDo
            }
            catch (Exception e)
            {
                _logger.LogError($"GetPrice, cog : {cog}. Error : {e}");
                return StatusCode(500);
            }
            return Ok();
        }


        [HttpGet]
        [Route("geoms")]
        public IActionResult GetGeoms()
        {
            try
            {
                // Get places
                var places = _pricemapContext.GeoPlaces.ToList();

                // Get prices per place
                var prices =
                    from prod in _pricemapContext.Listings
                    group prod by prod.PlaceId into g
                    select new
                    {
                        g.Key,
                        AveragePrice = g.Average(p => p.Price)
                    };

                return Ok(new FeatureCollection
                {
                    Type = ResponseType.FeatureCollection,
                    Features = places.Select(p => new Models.Features
                    {
                        Type = FeaturesType.Feature,
                        Properties = new Models.Properties
                        {
                            Cog = p.Cog,
                            Price = prices.FirstOrDefault(g => g.Key == int.Parse(p.Cog)) != null 
                            ? (int)prices.FirstOrDefault(g => g.Key == int.Parse(p.Cog)).AveragePrice 
                            : 0
                        }
                    })
                });
            }
            catch (Exception ex)
            {
                _logger.LogError($"GetGeoms : {ex}");
                return StatusCode(500);
            }
        }

        /// <summary>
        /// Action to collect data from listings api
        /// </summary>
        /// <returns></returns>
        [HttpPost]
        [Route("collect_data")]
        public async Task<IActionResult> CollectData()
        {
            try
            {
                var places = _pricemapContext.GeoPlaces.ToList();
                var tasks = new List<Task<IEnumerable<Listing>>>();
                foreach (var place in places)
                {
                    tasks.Add(_listingService.GetListings(place.Id));
                }
                Task.WaitAll(tasks.ToArray());
                for (var i = 0; i < places.Count; i++)
                {
                    foreach (var l in tasks[i].Result)
                    {
                        try
                        {
                            _pricemapContext.Listings.Add(new Infrastructure.Database.Model.Listing
                            {
                                ListingId = int.Parse(l.Id),
                                PlaceId = int.Parse(places[i].Cog),
                                RoomCount = 0,// ToDo use regex to extract room count
                                Area = 0,// ToDo use regex to extract room count
                                Price = l.Price != "Prix non communiqué" ? int.Parse(RemoveWiteSpaces(l.Price.Replace("€", ""))) : 0
                            });
                        }
                        catch (Exception e)
                        {
                            _logger.LogError($"GetGeoms : {e} ");
                        }

                    }
                }
                await _pricemapContext.SaveChangesAsync().ConfigureAwait(false);
            }
            catch (Exception e)
            {
                _logger.LogError($"GetGeoms : {e} ");
                return StatusCode(500);
            }
            return Ok();
        }

        private string RemoveWiteSpaces(string input)
        {
            return Regex.Replace(input, @"\s+", "");
        }
    }
}
