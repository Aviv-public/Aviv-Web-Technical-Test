using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using NetTopologySuite.Geometries;

namespace pricemap.Infrastructure.Database.Model
{
    [Table("geo_place")]
    public class GeoPlace
    {
        [Column("id")]
        [Key]
        public int Id { get; set; }
        [Column("cog")]
        public string Name { get; set; }
        [Column("geom")]
        public Geometry Geom { get; set; }
    }
}
