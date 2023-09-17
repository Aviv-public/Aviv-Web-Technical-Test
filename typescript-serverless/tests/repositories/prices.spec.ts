import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { getPriceRepository, PriceTableRow } from "@/repositories/prices";
import { Price } from "@/types.generated";
import PostgresClient from "serverless-postgres";
import { EntityNotFound } from "@/libs/errors";

class MockPostgresClient extends PostgresClient {
  query = vi.fn();
}

vi.mock("serverless-postgres", () => {
  return { default: MockPostgresClient };
});

describe("Price Repository", () => {
  let client: MockPostgresClient;
  let priceRepository: ReturnType<typeof getPriceRepository>;

  beforeEach(() => {
    client = new MockPostgresClient({});
    priceRepository = getPriceRepository(client);
  });

  afterEach(() => {
    vi.clearAllMocks();
  });

  it("should insert a new price successfully", async () => {
    const listingId = 1;
    const price: Price = {
      price_eur: 100000,
      created_date: new Date().toISOString(),
    };

    const mockPriceRow: PriceTableRow = {
      listing_id: listingId,
      price: price.price_eur,
      created_date: new Date(price.created_date),
    };

    client.query.mockImplementationOnce(() =>
      Promise.resolve({ rows: [mockPriceRow] })
    );

    const result = await priceRepository.insertPrice(listingId, price);

    expect(result).toEqual(price);
  });

  it("should get prices successfully", async () => {
    const listingId = 1;

    const mockPriceRows: PriceTableRow[] = [
      {
        listing_id: listingId,
        price: 100000,
        created_date: new Date(),
      },
      {
        listing_id: listingId,
        price: 500000,
        created_date: new Date(),
      },
      {
        listing_id: listingId,
        price: 150000,
        created_date: new Date(),
      },
    ];

    client.query.mockImplementation((queryString, queryValues) => {
      if (queryString === "SELECT * FROM price WHERE listing_id = $1") {
        const queriedListingId = queryValues[0];
        if (queriedListingId === listingId) {
          return Promise.resolve({ rows: mockPriceRows });
        } else {
          return Promise.resolve({ rows: [] });
        }
      }
    });

    const result = await priceRepository.getPrices(listingId);

    expect(result).toEqual(
      mockPriceRows.map((row) => ({
        price_eur: row.price,
        created_date: row.created_date.toISOString(),
      }))
    );
  });

  it("should throw an error when getting prices for a non-existent listing", async () => {
    const nonExistentListingId = 9999;

    client.query.mockImplementationOnce(() => Promise.resolve({ rows: [] }));

    await expect(
      priceRepository.getPrices(nonExistentListingId)
    ).rejects.toThrow(EntityNotFound);
  });

  it("should throw an error when inserting a price for a non-existent listing", async () => {
    const nonExistentListingId = 9999;
    const price: Price = {
      price_eur: 100000,
      created_date: new Date().toISOString(),
    };

    client.query.mockImplementationOnce(() => Promise.resolve({ rows: [] }));

    await expect(
      priceRepository.insertPrice(nonExistentListingId, price)
    ).rejects.toThrow(EntityNotFound);
  });

  it("should throw an error when inserting a price with a negative value", async () => {
    const listingId = 1;
    const price: Price = {
      price_eur: -100000,
      created_date: new Date().toISOString(),
    };

    client.query.mockImplementationOnce(() => Promise.resolve({ rows: [] }));

    await expect(
      priceRepository.insertPrice(listingId, price)
    ).rejects.toThrow();
  });
});
