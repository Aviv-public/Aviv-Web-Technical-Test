using NetTopologySuite.Geometries;
using System.ComponentModel.DataAnnotations.Schema;
using System.ComponentModel.DataAnnotations;
using Newtonsoft.Json;

namespace pricemap.Models
{
    public class FeatureCollection
    {
        [JsonProperty("type", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public ResponseType Type { get; set; }

        [JsonProperty("features", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public System.Collections.Generic.IEnumerable<Features> Features { get; set; }
    }

    public partial class Features
    {
        [JsonProperty("type", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        [JsonConverter(typeof(Newtonsoft.Json.Converters.StringEnumConverter))]
        public FeaturesType Type { get; set; }

        [JsonProperty("geometry", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public object Geometry { get; set; }

        [JsonProperty("properties", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public Properties Properties { get; set; }
    }

    public partial class Properties
    {
        [JsonProperty("cog", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public string Cog { get; set; }

        [JsonProperty("price", Required = Newtonsoft.Json.Required.DisallowNull, NullValueHandling = Newtonsoft.Json.NullValueHandling.Ignore)]
        public int Price { get; set; }
    }

    public enum ResponseType
    {
        [System.Runtime.Serialization.EnumMember(Value = @"FeatureCollection")]
        FeatureCollection = 0,

    }

    public enum FeaturesType
    {
        [System.Runtime.Serialization.EnumMember(Value = @"Feature")]
        Feature = 0,

    }
}
