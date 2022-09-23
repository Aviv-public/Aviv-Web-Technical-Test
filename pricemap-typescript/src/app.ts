import { Request, Response } from "express";
import { sql } from "./postgres";
import axios, { AxiosError } from "axios";

export async function updateData(req: Request, res: Response) {
  // TODO: this code is hard to get, it requires some refactoring
  const GEOMS_IDS = [
    32684, 32683, 32682, 32685, 32686, 32687, 32688, 32689, 32690, 32691, 32692,
    32693, 32699, 32694, 32695, 32696, 32697, 32698, 32700, 32701,
  ];

  await sql`
    CREATE TABLE IF NOT EXISTS listings (
      id INTEGER,
      place_id INTEGER,
      price INTEGER,
      area INTEGER,
      room_count INTEGER,
      seen_at TIMESTAMP,
      PRIMARY KEY (id, seen_at)
    )
  `;

  for (const geom of GEOMS_IDS) {
    let p = 0;

    while (true) {
      ++p;
      const url = `http://listingapi:5000/listings/${geom}?page=${p}`;

      let d;
      try {
        d = await axios.get(url);
      } catch (e) {
        if (e instanceof AxiosError && e.response?.status === 416) {
          break;
        }

        throw e;
      }

      for (const item of d.data) {
        const listingId = item["listing_id"];
        const roomCount = item["title"].includes("Studio")
          ? 1
          : !item["title"].includes("pièces")
          ? 0
          : Number.parseInt(
              (item["title"].split("pièces")[0] as string)
                .split("")
                .filter((letter) => !Number.isNaN(Number.parseInt(letter)))
                .join("")
            ) || 0;

        const price =
          Number.parseInt(
            (item["price"] as string)
              .split("")
              .filter((letter) => !Number.isNaN(Number.parseInt(letter)))
              .join("")
          ) || 0;

        const areaText = (item["title"].split("-")[1] || "0")
          .replaceAll(" ", "")
          .replaceAll("\u00a0m\u00b2", "");

        const area = Number.parseInt(areaText);

        const seenAt = Math.round(Date.now() / 1000);

        await sql`
          INSERT INTO listings VALUES(
            ${listingId},
            ${geom},
            ${price},
            ${area},
            ${roomCount},
            ${seenAt}
          )
        `;
      }
    }
  }

  res.status(200);
  res.send();
}
