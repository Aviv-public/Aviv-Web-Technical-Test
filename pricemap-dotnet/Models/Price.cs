using Newtonsoft.Json;
using System;

namespace pricemap.Models
{
    public partial class Price
    {
        /// <summary>A price, expressed in euros.</summary>
        [JsonProperty("price_eur")]
        public int Price_eur { get; set; }
    }
}
