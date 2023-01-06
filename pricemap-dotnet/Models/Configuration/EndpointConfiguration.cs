using Newtonsoft.Json;
using System;
using System.Collections.Generic;

namespace pricemap.Services.Model.Configuration
{
    public class EndpointConfiguration
    {
        [JsonProperty("baseUrl")]
        public string BaseUrl { get; init; } = String.Empty;

        [JsonProperty("apiKey")]
        public string ApiKey { get; init; } = String.Empty;

        [JsonProperty("timeout")]
        public int Timeout { get; init; } = 5;
    }
}
