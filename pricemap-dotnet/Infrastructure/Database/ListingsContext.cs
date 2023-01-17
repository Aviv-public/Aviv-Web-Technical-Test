using Microsoft.EntityFrameworkCore;
using pricemap.Infrastructure.Database.Models;

namespace pricemap.Infrastructure.Database
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
        public virtual DbSet<Price> Prices { get; set; }
    }
}
