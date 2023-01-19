using System;
using System.Text.Json.Serialization;

namespace listingapi.Models
{
    public partial class ListingReadOnly
    {
        [JsonPropertyName("id")]
        public long Id { get; set; }

        [JsonPropertyName("created_date")]
        public DateTime CreatedDate { get; set; }

        [JsonPropertyName("updated_date")]
        public DateTime UpdatedDate { get; set; }

        [JsonPropertyName("price")]
        public PriceReadOnly Price { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; }

        [JsonPropertyName("postal_address")]
        public PostalAddress PostalAddress { get; set; }

        [JsonPropertyName("description")]
        public string Description { get; set; }

        [JsonPropertyName("building_type")]
        public string BuildingType { get; set; }

        [JsonPropertyName("surface_area_m2")]
        public double SurfaceAreaM2 { get; set; }

        [JsonPropertyName("rooms_count")]
        public int RoomsCount { get; set; }

        [JsonPropertyName("bedrooms_count")]
        public int BedroomsCount { get; set; }

        [JsonPropertyName("contact_phone_number")]
        public string ContactPhoneNumber { get; set; }
    }
}
