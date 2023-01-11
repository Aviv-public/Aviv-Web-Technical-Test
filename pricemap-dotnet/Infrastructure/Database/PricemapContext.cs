using Microsoft.EntityFrameworkCore;
using pricemap.Infrastructure.Database.Model;

namespace pricemap.Infrastructure.Database
{
    public class PricemapContext : DbContext
    {
        public PricemapContext(DbContextOptions<PricemapContext> options) : base(options)
        {

        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<GeoPlace>().ToTable("geo_place", t => t.ExcludeFromMigrations());
        }

        public DbSet<Listing> Listings { get; set; }
        public DbSet<Price> Prices { get; set; }
        public DbSet<View> Views { get; set; }
        public DbSet<GeoPlace> GeoPlaces { get; set; }
    }
}
