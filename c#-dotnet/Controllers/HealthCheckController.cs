using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;
using listingapi.Infrastructure.Database;

namespace listingapi.Controllers
{
    [ApiController]
    public class HealthCheckController : ControllerBase
    {
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
            return Ok("OK");
        }
    }
}
