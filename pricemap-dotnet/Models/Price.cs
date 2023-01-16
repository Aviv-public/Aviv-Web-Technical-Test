using System;

namespace pricemap.Models
{
    public partial class Price
    {
        /// <summary>A price, expressed in euros.</summary>
        [Newtonsoft.Json.JsonProperty("price_eur", Required = Newtonsoft.Json.Required.Always)]
        public int Price_eur { get; set; }

        /// <summary>The date at which the price was published.</summary>
        [Newtonsoft.Json.JsonProperty("date_posted", Required = Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DataAnnotations.Required(AllowEmptyStrings = true)]
        public DateTime Date_posted { get; set; }
    }
}
