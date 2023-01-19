using Microsoft.EntityFrameworkCore;
using listingapi.Infrastructure.Database.Models;

namespace listingapi.Infrastructure.Database
{
    public class ListingsContext : DbContext
    {
        public ListingsContext(DbContextOptions<ListingsContext> options) : base(options)
        {

        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
        }

        public virtual DbSet<Listing> Listings { get; set; }
    }
}
