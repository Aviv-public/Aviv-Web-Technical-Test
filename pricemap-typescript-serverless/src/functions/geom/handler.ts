import { formatJSONResponse } from '@libs/api-gateway';
import { sql } from "@libs/postgres";
import { FeatureCollection } from "../../types.generated";

const geom = async () => {
  const results = await sql`
    SELECT
      ST_ASGEOJSON(geom) as geom,
      cog,
      sum(price) / sum(area) as price
    FROM geo_place
    JOIN listings ON geo_place.id = listings.place_id
    group by (geom, cog)
  `;

  console.log(results)

  const geoms: FeatureCollection = {
    type: "FeatureCollection",
    features: [],
  };

  for (const row of results) {
    const geometry = {
      type: "Feature" as const,
      geometry: JSON.parse(row["geom"]),
      properties: {
        cog: row["cog"],
        price: row["price"],
      },
    };

    geoms["features"].push(geometry);
  }

  return formatJSONResponse(geoms);
};

export const main = geom;
