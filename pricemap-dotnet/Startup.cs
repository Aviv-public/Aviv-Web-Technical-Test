using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.OpenApi.Models;
using pricemap.Configuration;
using pricemap.Infrastructure.Database;
using pricemap.Services.Contracts;
using pricemap.Services.Implem;
using pricemap.Services.Model.Configuration;
using System;

namespace pricemap
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            var pricemapConfig = Configuration.GetSection("dataBase:pricemap").Get<Infrastructure.Database.Model.DataBaseConfiguration>();
            services.AddDbContext<PricemapContext>(options =>
            {
                options.UseNpgsql(pricemapConfig.ToString(),
                    npgsqlOptionsAction: sqlOptions =>
                    {
                        sqlOptions.CommandTimeout(60);
                        //sqlOptions.EnableRetryOnFailure(
                        //    maxRetryCount: 5,
                        //    maxRetryDelay: TimeSpan.FromSeconds(3),
                        //    errorCodesToAdd: null);
                        sqlOptions.UseQuerySplittingBehavior(QuerySplittingBehavior.SingleQuery);
                    });
            });
            var listingsapiEndpoint = Configuration.GetSection("endPoints:listingsapi").Get<EndpointConfiguration>();
            services.AddHttpClient<IListingService, ListingService>(client =>
            {
                client.BaseAddress = new Uri(listingsapiEndpoint.BaseUrl);
                client.Timeout = TimeSpan.FromSeconds(listingsapiEndpoint.Timeout);
            });
            
            services.AddMemoryCache();

            services.AddControllers(options =>
            {
                options.Conventions.Add(new GroupingByNamespaceConvention());
            });

            services.AddSwaggerGen(c =>
            {
                c.SwaggerDoc("v1", new OpenApiInfo { Title = "pricemap v1", Version = "v1" });
                c.CustomSchemaIds(type => type.ToString());
            });
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (!env.IsProduction())
            {
                app.UseDeveloperExceptionPage();
            }

            app.UseSwagger();
            app.UseSwaggerUI(c =>
            {
                c.SwaggerEndpoint("/swagger/v1/swagger.json", "pricemap v1");
            }
            );

            app.UseHttpsRedirection();

            app.UseRouting();

            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });
        }
    }
}
