using pricemap.Services.Contracts.V1;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace pricemap.Controllers.V1
{
    [Route("api/v1/pricemap")]
    public class PricemapController : ControllerBase
    {
        #region Properties

        private readonly ILogger<PricemapController> _logger;

        public PricemapController(ILogger<PricemapController> logger)
        {
            _logger = logger;
        }
        #endregion

        [HttpGet]
        //[ProducesResponseType(typeof(), StatusCodes.Status200OK)]
        public async Task<IActionResult> Get(int id)
        {
            if (id < 0) return BadRequest();
            try
            {
                // ToDo
            }
            catch (Exception e)
            {
                if (e.GetType().Name.Equals("ArgumentOutOfRangeException"))
                {
                    _logger.LogError($"Index : id : {id} ");
                    return BadRequest();
                }

                _logger.LogError($"Get : {id} : {e} ");
                return StatusCode(500);
            }
            return Ok();
        }
    }
}
