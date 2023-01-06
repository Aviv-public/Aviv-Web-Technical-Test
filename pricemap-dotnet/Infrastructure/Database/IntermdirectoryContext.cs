using Microsoft.EntityFrameworkCore;

namespace pricemap.Infrastructure.Database
{
    public class PricemapContext : DbContext
    {
        public PricemapContext(DbContextOptions<PricemapContext> options) : base(options)
        {

        }
        
        // ToDo put here set of data
        //public DbSet<Intermediary> Intermediaries { get; set; }
    }
}
