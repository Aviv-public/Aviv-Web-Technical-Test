using Microsoft.AspNetCore.Mvc;

namespace pricemap.Controllers
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
