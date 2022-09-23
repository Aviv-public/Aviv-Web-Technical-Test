import { Request, Response } from "express";
import { sql } from "./postgres";

export async function geoms(req: Request, res: Response) {
  // TODO: you can tweak the query and/or the code if you think it's needed
  const results = await sql`
    SELECT
      ST_ASGEOJSON(geom) as geom,
      cog,
      sum(price) / sum(area) as price
    FROM geo_place
    JOIN listings ON geo_place.id = listings.place_id
    group by (geom, cog)
  `;

  const geoms = {
    type: "FeatureCollection",
    features: [],
  };

  for (const row of results) {
    const geometry = {
      type: "Feature",
      geometry: JSON.parse(row["geom"]),
      properties: {
        cog: row["cog"],
        price: row["price"],
      },
    };

    // @ts-expect-error looks like this should be improved a bit...
    geoms["features"].push(geometry);
  }

  res.json(geoms);
}

/**
 * Returns the volumes distribution for the given cog in storage format
 */
export async function getPrice(req: Request, res: Response) {
  // TODO: we can do a better histogram (better computation, better volume and labels, etc.)
  const serieName = `Prix ${req.params.cog}`;

  type Labels = { [key: string]: number };
  const labels: Labels = {
    "0-6000": 0,
    "6000-8000": 0,
    "8000-10000": 0,
    "10000-14000": 0,
    "14000-100000": 0,
  };

  for (const label of Object.keys(labels)) {
    const minPrice = label.split("-")[0];
    const maxPrice = label.split("-")[1];

    const results = await sql`
      SELECT
       ST_ASGEOJSON(geom) as geom,
       cog,
       area,
       price
     FROM geo_place
     JOIN listings ON geo_place.id = listings.place_id
     WHERE area != 0 AND price / area > ${minPrice} AND price / area < ${maxPrice}
   `;

    labels[label] = results.length;
  }

  res.json({
    serie_name: serieName,
    volumes: Object.values(labels),
    labels: Object.keys(labels),
  });
}
