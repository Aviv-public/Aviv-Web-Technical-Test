using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;
using pricemap.Services.Contracts;
using pricemap.Services.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Reflection.Emit;
using System.Reflection.PortableExecutable;
using System.Threading.Tasks;

namespace pricemap.Services.Implem
{
    public class ListingService : IListingService
    {
        private readonly HttpClient _httpClient;
        private readonly ILogger<ListingService> _logger;
        private const int PAGE_SIZE = 20;

        public ListingService(HttpClient httpClient, ILogger<ListingService> logger)
        {
            _httpClient = httpClient;
            _logger = logger;
        }

        public async Task<IEnumerable<Listing>> GetListings(int placeId)
        {
            if (placeId <= 0) throw new ArgumentException("placeId is null or not a int");
            var page = 0;
            var listings = new List<Listing>();
            var listingsPerPage = await GetListings(placeId, page).ConfigureAwait(false);
            while (listingsPerPage != null && listingsPerPage.Count() == PAGE_SIZE)
            {
                listings.AddRange(listingsPerPage);
                listingsPerPage = await GetListings(placeId, ++page).ConfigureAwait(false);
            }
            return listings;
        }

        /// <summary>
        /// Retrive listings per page
        /// </summary>
        /// <param name="placeId"></param>
        /// <param name="page"></param>
        /// <returns></returns>
        private async Task<IEnumerable<Listing>> GetListings(int placeId, int page)
        {
            var m = $"/listings/{placeId}?page={page}";
            try
            {
                var httpRequestMessage = new HttpRequestMessage(HttpMethod.Get, new Uri($"{_httpClient.BaseAddress}{m}"));
                var response = await _httpClient.SendAsync(httpRequestMessage).ConfigureAwait(false);
                if (response == null || response.StatusCode == System.Net.HttpStatusCode.NotFound) return null;
                response.EnsureSuccessStatusCode();
                var responseContentString = await response.Content.ReadAsStringAsync().ConfigureAwait(false);
                var r = JsonConvert.DeserializeObject<IEnumerable<Listing>>(responseContentString);
                return r;
            }
            catch (Exception ex)
            {
                _logger.LogError("ErrorGetListings", ex);
            }
            return new List<Listing>();

        }
    }
}
