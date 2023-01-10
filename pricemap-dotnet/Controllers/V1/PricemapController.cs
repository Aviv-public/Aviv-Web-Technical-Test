using pricemap.Services.Contracts;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace pricemap.Controllers.V1
{
    [Route("api/v1")]
    public class PricemapController : ControllerBase
    {
        #region Properties

        private readonly ILogger<PricemapController> _logger;

        public PricemapController(ILogger<PricemapController> logger)
        {
            _logger = logger;
        }
        #endregion

        /// <summary>
        /// 
        /// </summary>
        /// <param name="cog">cog the place</param>
        /// <returns></returns>
        [HttpGet]
        [Route("get_price/{placeId}")]
        public async Task<IActionResult> GetPrice(string cog)
        {
            if (string.IsNullOrEmpty(cog)) return BadRequest();
            try
            {
                // ToDo
            }
            catch (Exception e)
            {
                _logger.LogError($"GetPrice, cog : {cog}. Error : {e}");
                return StatusCode(500);
            }
            return Ok();
        }


        [HttpGet]
        [Route("geoms")]
        public async Task<IActionResult> GetGeoms()
        {
            try
            {
                // ToDo
            }
            catch (Exception e)
            {
                _logger.LogError($"GetGeoms : {e} ");
                return StatusCode(500);
            }
            return Ok();
        }

        /// <summary>
        /// Action to collect data from listings api
        /// </summary>
        /// <returns></returns>
        [HttpPost]
        [Route("collect_data")]
        public async Task<IActionResult> CollectData()
        {
            try
            {
                // ToDo
            }
            catch (Exception e)
            {
                _logger.LogError($"GetGeoms : {e} ");
                return StatusCode(500);
            }
            return Ok();
        }


    }
}
