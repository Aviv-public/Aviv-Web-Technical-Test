using NetTopologySuite.Geometries;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace pricemap.Infrastructure.Database.Model
{
    [Table("geo_place")]
    public class GeoPlace
    {
        [Column("id")]
        [Key]
        public int Id { get; set; }
        [Column("cog")]
        public string Cog { get; set; }
        [Column("geom")]
        [NotMapped]
        public Geometry Geom { get; set; }
    }
}
