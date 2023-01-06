using System;
using System.ComponentModel.DataAnnotations.Schema;

namespace pricemap.Infrastructure.Database.Model
{
    public class PriceHistory
    {
        [Column("listing_id")]
        public string ListingId { get; set; }
        [Column("price")]
        public int Price { get; set; }
        [Column("price_date")]
        public DateTime PriceDate { get; set; }
    }
}
