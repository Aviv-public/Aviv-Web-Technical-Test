using Microsoft.EntityFrameworkCore;

namespace pricemap.Infrastructure.Database
{
    public class PricemapWriteContext : DbContext
    {
        public PricemapWriteContext(DbContextOptions<PricemapWriteContext> options) : base(options)
        {

        }
    }
}
