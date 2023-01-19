using System.Text.Json.Serialization;

namespace listingapi.Models
{
    public partial class PostalAddress
    {
        [JsonPropertyName("street_address")]
        public string StreetAddress { get; set; }

        [JsonPropertyName("postal_code")]
        public string PostalCode { get; set; }

        [JsonPropertyName("city")]
        public string City { get; set; }

        [JsonPropertyName("country")]
        public string Country { get; set; }
    }
}
