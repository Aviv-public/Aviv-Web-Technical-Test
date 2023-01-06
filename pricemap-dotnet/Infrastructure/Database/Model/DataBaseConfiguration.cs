using Newtonsoft.Json;

namespace pricemap.Infrastructure.Database.Model
{
    public class DataBaseConfiguration
    {
        [JsonProperty("host")]
        public string? Host { get; set; }

        [JsonProperty("databaseName")]
        public string? DatabaseName { get; set; }

        [JsonProperty("userName")]
        public string? UserName { get; set; }

        [JsonProperty("password")]
        public string? Password { get; set; }

        [JsonProperty("port")]
        public long Port { get; set; }

        public override string ToString()
        {
            return $"Host={Host};port={Port};Username={UserName};Password={Password};Database={DatabaseName};";
        }
    }

    public partial class Databases
    {
        [JsonProperty("pricemap")]
        public DataBaseConfiguration? Pricemap { get; set; }
    }
}
