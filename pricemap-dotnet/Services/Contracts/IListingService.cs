using pricemap.Services.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace pricemap.Services.Contracts
{
    public interface IListingService
    {
        Task<IEnumerable<Listing>> GetListings(int placeId);
    }
}
