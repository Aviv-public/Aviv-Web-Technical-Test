using Newtonsoft.Json;

namespace pricemap.Models
{
    public partial class PostalAddress
    {
        [JsonProperty("street_address")]
        public string StreetAddress { get; set; }

        [JsonProperty("postal_code")]
        public string PostalCode { get; set; }

        [JsonProperty("city")]
        public string City { get; set; }

        [JsonProperty("country")]
        public string Country { get; set; }
    }
}
