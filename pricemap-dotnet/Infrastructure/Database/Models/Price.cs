using System;
using System.ComponentModel.DataAnnotations.Schema;

namespace pricemap.Infrastructure.Database.Models
{
    [Table("prices")]
    public class Price : BaseEntity
    {
        [Column("listing_id")]
        public int ListingId { get; set; }
        [Column("price")]
        public int PriceValue { get; set; }
        [Column("price_date")]
        public DateTime PriceDate { get; set; }
    }
}
