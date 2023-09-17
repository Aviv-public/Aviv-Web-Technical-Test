import { functionHandler } from "@/libs/function";
import { getRepository } from "@/repositories/listings";
import { Listing, ListingWrite } from "@/types.generated";
import { EntityNotFound, NotFound } from "@/libs/errors";
import { getPriceRepository } from "@/repositories/prices";

export const getListings = functionHandler<Listing[]>(
  async (_event, context) => {
    const listings = await getRepository(context.postgres).getAllListings();

    return { statusCode: 200, response: listings };
  }
);

export const addListing = functionHandler<Listing, ListingWrite>(
  async (event, context) => {
    const listing = await getRepository(context.postgres).insertListing(
      event.body
    );

    const price = {
      price_eur: event.body.latest_price_eur,
      created_date: new Date().toISOString(),
    };
    await getPriceRepository(context.postgres).insertPrice(listing.id, price);

    return { statusCode: 201, response: listing };
  }
);

export const updateListing = functionHandler<Listing, ListingWrite>(
  async (event, context) => {
    try {
      const id = parseInt(event.pathParameters.id);
      const newPrice = event.body.latest_price_eur;

      const currentListing = await getRepository(context.postgres).getListing(
        id
      );

      const listing = await getRepository(context.postgres).updateListing(
        id,
        event.body
      );

      if (currentListing.latest_price_eur !== newPrice) {
        const price = {
          price_eur: newPrice,
          created_date: new Date().toISOString(),
        };
        await getPriceRepository(context.postgres).insertPrice(id, price);
      }

      return { statusCode: 200, response: listing };
    } catch (e) {
      if (e instanceof EntityNotFound) {
        throw new NotFound(e.message);
      }

      throw e;
    }
  }
);
