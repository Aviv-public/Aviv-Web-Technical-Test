using Serilog.Core;
using Serilog.Events;
using System.Diagnostics;

namespace pricemap.Serilog
{
    public class W3CTraceContextEnricher : ILogEventEnricher
    {
        public void Enrich(LogEvent logEvent, ILogEventPropertyFactory propertyFactory)
        {
            var activity = Activity.Current;
            if (activity?.IdFormat is ActivityIdFormat.W3C)
            {
                logEvent.AddPropertyIfAbsent(propertyFactory.CreateProperty("TraceId", activity.TraceId.ToHexString()));
                if (activity.ParentSpanId != default)
                {
                    logEvent.AddPropertyIfAbsent(propertyFactory.CreateProperty("ParentId", activity.ParentSpanId.ToHexString()));
                }
                logEvent.AddPropertyIfAbsent(propertyFactory.CreateProperty("SpanId", activity.SpanId.ToHexString()));
            }
        }
    }
}
