import PostgresClient from "serverless-postgres";
import { Price } from "@/types.generated";
import { extractVariables } from "@/libs/postgres";
import { EntityNotFound } from "@/libs/errors";

export type PriceTableRow = {
  id?: number;
  listing_id: number;
  price: number;
  created_date: Date;
};

function tableRowToPrice(row: PriceTableRow): Price {
  return {
    price_eur: row.price,
    created_date: row.created_date.toISOString(),
  };
}

function priceToTableRow(price: Price, listingId: number): PriceTableRow {
  return {
    listing_id: listingId,
    price: price.price_eur,
    created_date: new Date(price.created_date),
  };
}

export function getPriceRepository(postgres: PostgresClient) {
  return {
    async insertPrice(listingId: number, price: Price) {
      const tableRow = priceToTableRow(price, listingId);
      const {
        columns,
        variables,
        values: queryValues,
      } = extractVariables(tableRow);
      const queryString = `
      INSERT INTO price (${columns.join(", ")}) 
      VALUES (${variables}) 
      RETURNING *
      `;

      const result = await postgres.query(queryString, queryValues);
      const addedPrice = result.rows[0];

      if (!addedPrice) {
        throw new EntityNotFound(
          `Could not add price for listing with id: ${listingId}`
        );
      }
      return tableRowToPrice(addedPrice);
    },

    async getPrices(listingId: number): Promise<Price[]> {
      const queryString = `SELECT * FROM price WHERE listing_id = $1`;
      const queryValues = [listingId];

      const result = await postgres.query(queryString, queryValues);
      const prices = result.rows;

      if (!prices.length) {
        throw new EntityNotFound(
          `Could not find prices for listing with id: ${listingId}`
        );
      }

      return prices.map(tableRowToPrice);
    },
  };
}
