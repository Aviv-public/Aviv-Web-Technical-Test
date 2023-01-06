using System;
using System.ComponentModel.DataAnnotations.Schema;

namespace pricemap.Infrastructure.Database.Model
{
    public class PriceView
    {
        [Column("listing_id")]
        public string ListingId { get; set; }
        [Column("view_date")]
        public DateTime ViewDate { get; set; }
    }
}
