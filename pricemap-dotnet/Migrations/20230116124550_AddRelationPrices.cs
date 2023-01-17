using Microsoft.EntityFrameworkCore.Migrations;

namespace pricemap.Migrations
{
    public partial class AddRelationPrices : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateIndex(
                name: "IX_prices_listing_id",
                table: "prices",
                column: "listing_id");

            migrationBuilder.AddForeignKey(
                name: "FK_prices_listings_listing_id",
                table: "prices",
                column: "listing_id",
                principalTable: "listings",
                principalColumn: "id",
                onDelete: ReferentialAction.Cascade);
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropForeignKey(
                name: "FK_prices_listings_listing_id",
                table: "prices");

            migrationBuilder.DropIndex(
                name: "IX_prices_listing_id",
                table: "prices");
        }
    }
}
