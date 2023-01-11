using Newtonsoft.Json;

namespace pricemap.Services.Models
{
    public class Listing
    {
        [JsonProperty("listing_id")]
        public string Id { get; set; }
        [JsonProperty("place")]
        public string Place { get; set; }
        [JsonProperty("price")]
        public string Price { get; set; }
        [JsonProperty("title")]
        public string Title { get; set; }
    }
}
