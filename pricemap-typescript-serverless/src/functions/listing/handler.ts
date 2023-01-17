import { functionHandler } from "@/libs/function";
import { getRepository } from "@/repositories/listings";
import { Listing, ListingReadOnly } from "@/types.generated";
import { EntityNotFound, NotFound } from "@/libs/errors";

export const getListings = functionHandler<(Listing & ListingReadOnly)[]>(
  async (_event, context) => {
    const listings = await getRepository(context.postgres).getAllListings();

    return { statusCode: 200, response: listings };
  }
);

export const addListing = functionHandler<Listing & ListingReadOnly>(
  async (event, context) => {
    const listing = await getRepository(context.postgres).insertListing(
      event.body
    );

    return { statusCode: 201, response: listing };
  }
);

export const updateListing = functionHandler<Listing & ListingReadOnly>(
  async (event, context) => {
    try {
      const listing = await getRepository(context.postgres).updateListing(
        parseInt(event.pathParameters.id),
        event.body
      );

      return { statusCode: 200, response: listing };
    } catch (e) {
      if (e instanceof EntityNotFound) {
        throw new NotFound(e.message);
      }

      throw e;
    }
  }
);
