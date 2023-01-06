using Microsoft.AspNetCore.Mvc;

namespace pricemap.Controllers
{
    [ApiController]
    public class HealthCheckController : ControllerBase
    {
        [HttpGet]
        [Route("healthcheck.html")]
        public IActionResult Get()
        {
            return Ok("OK");
        }

        [HttpGet]
        [Route("readiness.html")]
        public IActionResult GetReadiness()
        {
            return Ok("OK");
        }
    }
}
