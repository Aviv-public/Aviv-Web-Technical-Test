using Serilog;
using Serilog.Formatting.Json;

namespace pricemap.Serilog
{
    public static class LoggerConfigurationExtensions
    {
        public static LoggerConfiguration ConfigureDefault(this LoggerConfiguration loggerConfiguration) =>
            loggerConfiguration
        .MinimumLevel.Information()
        // The W3CTraceContextEnricher enricher will likely be useless with the next
        // version of Serilog.AspNetCore. See this issue:
        // https://github.com/serilog/serilog-aspnetcore/issues/207
        .Enrich.With<W3CTraceContextEnricher>()
        .WriteTo.Console(new JsonFormatter(renderMessage: true));
    }
}
