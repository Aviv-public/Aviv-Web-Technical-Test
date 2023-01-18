using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using listingapi.Infrastructure.Database;

namespace listingapi.Controllers
{
    [ApiController]
    public class HealthCheckController : ControllerBase
    {
        #region Properties
        private readonly ListingsContext _listingsContext;
        private readonly ILogger<HealthCheckController> _logger;

        public HealthCheckController(ILogger<HealthCheckController> logger, ListingsContext listingsContext)
        {
            _logger = logger;
            _listingsContext = listingsContext;
        }
        #endregion

        [HttpGet]
        [Route("healthcheck")]
        public IActionResult Get()
        {
            return Ok("OK");
        }

        [HttpGet]
        [Route("readiness")]
        public IActionResult GetReadiness()
        {
            try
            {
                _listingsContext.Database.ExecuteSqlRaw("SELECT 1");
                return Ok("OK");
            }
            catch
            {
                return StatusCode(503);
            }
        }
    }
}
