namespace pricemap.Models
{
    public class Serie
    {
        [Newtonsoft.Json.JsonProperty("serie_name", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public string SerieName { get; set; }

        [Newtonsoft.Json.JsonProperty("volumes", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public System.Collections.Generic.IEnumerable<int> Volumes { get; set; }

        [Newtonsoft.Json.JsonProperty("labels", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public System.Collections.Generic.IEnumerable<string> Labels { get; set; }
    }
}
