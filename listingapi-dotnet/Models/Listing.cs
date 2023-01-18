using System.Text.Json.Serialization;

namespace listingapi.Models
{
    public partial class Listing
    {
        [JsonPropertyName("name")]
        public string Name { get; set; }

        [JsonPropertyName("postal_address")]
        public PostalAddress PostalAddress { get; set; }

        [JsonPropertyName("description")]
        public string Description { get; set; }

        [JsonPropertyName("building_type")]
        [JsonConverter(typeof(JsonStringEnumConverter))]
        public RealEstateListingBuildingType BuildingType { get; set; }

        [JsonPropertyName("latest_price_eur")]
        public int LatestPriceEur { get; set; }

        [JsonPropertyName("surface_area_m2")]
        public int SurfaceAreaM2 { get; set; }

        [JsonPropertyName("rooms_count")]
        public int RoomsCount { get; set; }

        [JsonPropertyName("bedrooms_count")]
        public int BedroomsCount { get; set; }

        [JsonPropertyName("contact_phone_number")]
        public string ContactPhoneNumber { get; set; }
    }

    public enum RealEstateListingBuildingType
    {
        [System.Runtime.Serialization.EnumMember(Value = @"STUDIO")]
        STUDIO = 0,

        [System.Runtime.Serialization.EnumMember(Value = @"APARTMENT")]
        APARTMENT = 1,

        [System.Runtime.Serialization.EnumMember(Value = @"HOUSE")]
        HOUSE = 2,

    }

    public partial class ListingPrice
    {
        [JsonPropertyName("last_price_eur")]
        public int LastPriceEur { get; set; }
    }
}
