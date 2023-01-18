using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using listingapi.Configuration;
using listingapi.Infrastructure.Database;
using listingapi.Infrastructure.Database.Models;

namespace listingapi
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
            var listingApiConfig = Configuration.GetSection("dataBase:listingApi").Get<DataBaseConfiguration>();
            services.AddDbContext<ListingsContext>(options =>
            {
                options.UseNpgsql(listingApiConfig.ToString(),
                    npgsqlOptionsAction: sqlOptions =>
                    {
                        sqlOptions.CommandTimeout(60);
                        sqlOptions.UseQuerySplittingBehavior(QuerySplittingBehavior.SingleQuery);
                    });
            });

            services.AddControllers(options =>
            {
                options.Conventions.Add(new GroupingByNamespaceConvention());
            });
            services.AddSwaggerGen();
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (!env.IsProduction())
            {
                app.UseDeveloperExceptionPage();
                app.UseSwagger();
                app.UseSwaggerUI();
            }

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
