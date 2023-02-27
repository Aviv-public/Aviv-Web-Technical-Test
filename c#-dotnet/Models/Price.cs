using Newtonsoft.Json;

namespace listingapi.Models
{
    public partial class Price
    {
        /// <summary>A price, expressed in euros.</summary>
        [JsonProperty("price_eur")]
        public int PriceEur { get; set; }
    }
}
