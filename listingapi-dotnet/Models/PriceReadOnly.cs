using System;
using System.Text.Json.Serialization;

namespace listingapi.Models
{
    public partial class PriceReadOnly : Price
    {
        [JsonPropertyName("created_date")]
        public DateTime CreatedDate { get; set; }
    }
}
