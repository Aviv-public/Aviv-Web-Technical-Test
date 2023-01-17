using System.Text.Json.Serialization;

namespace pricemap.Infrastructure.Database.Models
{
    public class DataBaseConfiguration
    {
        [JsonPropertyName("host")]
        public string? Host { get; set; }

        [JsonPropertyName("databaseName")]
        public string? DatabaseName { get; set; }

        [JsonPropertyName("userName")]
        public string? UserName { get; set; }

        [JsonPropertyName("password")]
        public string? Password { get; set; }

        [JsonPropertyName("port")]
        public long Port { get; set; }

        public override string ToString()
        {
            return $"Host={Host};port={Port};Username={UserName};Password={Password};Database={DatabaseName};";
        }
    }

    public partial class Databases
    {
        [JsonPropertyName("pricemap")]
        public DataBaseConfiguration? Pricemap { get; set; }
    }
}
