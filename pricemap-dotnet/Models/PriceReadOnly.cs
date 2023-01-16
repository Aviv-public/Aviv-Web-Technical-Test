using Newtonsoft.Json;
using System;

namespace pricemap.Models
{
    public class PriceReadOnly : Price
    {
        [JsonProperty("created_date")]
        public DateTime CreatedDate { get; set; }
    }
}
