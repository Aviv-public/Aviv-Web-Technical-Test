using System.Text.Json.Serialization;

namespace pricemap.Models
{
    public partial class Price
    {
        /// <summary>A price, expressed in euros.</summary>
        [JsonPropertyName("price_eur")]
        public int PriceEur { get; set; }
    }
}
