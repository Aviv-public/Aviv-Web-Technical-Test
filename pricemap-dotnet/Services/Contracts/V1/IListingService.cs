using System.Collections.Generic;
using System.Threading.Tasks;

namespace pricemap.Services.Contracts.V1
{
    public interface IListingService
    {
        // ToDo
        Task<List<object>> GetListings();
    }
}
