using Newtonsoft.Json;
using System;

namespace listingapi.Models
{
    public partial class ListingReadOnly
    {
        [JsonProperty("id")]
        public long Id { get; set; }

        [JsonProperty("created_date")]
        public DateTime CreatedDate { get; set; }

        [JsonProperty("updated_date")]
        public DateTime UpdatedDate { get; set; }

        [JsonProperty("price")]
        public PriceReadOnly Price { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("postal_address")]
        public PostalAddress PostalAddress { get; set; }

        [JsonProperty("description")]
        public string Description { get; set; }

        [JsonProperty("building_type")]
        public string BuildingType { get; set; }

        [JsonProperty("surface_area_m2")]
        public double SurfaceAreaM2 { get; set; }

        [JsonProperty("rooms_count")]
        public int RoomsCount { get; set; }

        [JsonProperty("bedrooms_count")]
        public int BedroomsCount { get; set; }

        [JsonProperty("contact_phone_number")]
        public string ContactPhoneNumber { get; set; }
    }
}
