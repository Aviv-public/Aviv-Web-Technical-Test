using pricemap.Serilog;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using Serilog;

namespace pricemap
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureAppConfiguration((hostingContext, configuration) =>
                {
                    IHostEnvironment env = hostingContext.HostingEnvironment;
                    configuration
                        .AddJsonFile("appsettings.json", optional: true, reloadOnChange: true)
                        .AddJsonFile($"appsettings.{env.EnvironmentName}.json", true, true)
                        .AddJsonFile($"secret.json", true, true);
                    IConfigurationRoot configurationRoot = configuration.Build();
                })
                .ConfigureLogging((hosting, logging) =>
                {
                    var logger = new LoggerConfiguration()
                        .ConfigureDefault()
                        .ReadFrom.Configuration(hosting.Configuration)
                        .CreateLogger();

                    logging
                        .ClearProviders()
                        .AddSerilog(logger, dispose: true);
                })
                .ConfigureWebHostDefaults(webBuilder => { webBuilder.UseStartup<Startup>(); })
        ;
    }
}
