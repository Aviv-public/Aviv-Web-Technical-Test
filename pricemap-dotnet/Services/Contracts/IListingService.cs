using System.Collections.Generic;
using System.Threading.Tasks;

namespace pricemap.Services.Contracts
{
    public interface IListingService
    {
        // ToDo
        Task<List<object>> GetListings();
    }
}
