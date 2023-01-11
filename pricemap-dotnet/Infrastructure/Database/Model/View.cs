using System;
using System.ComponentModel.DataAnnotations.Schema;

namespace pricemap.Infrastructure.Database.Model
{
    [Table("views")]
    public class View : BaseEntity
    {
        [Column("listing_id")]
        public int ListingId { get; set; }
        [Column("view_date")]
        public DateTime ViewDate { get; set; }
    }
}
