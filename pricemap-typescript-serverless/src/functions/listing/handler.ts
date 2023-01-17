import { functionHandler } from "@/libs/function";
import { getRepository } from "@/repositories/listings";
import { Listing, ListingReadOnly } from "@/types.generated";

export const getListings = functionHandler<(Listing & ListingReadOnly)[]>(
  async (event, context) => {
    const listings = await getRepository(context.postgres).getAllListings();

    return { statusCode: 200, response: listings };
  }
);

export const addListing = functionHandler<Listing & ListingReadOnly>(
  async (event, context) => {
    const listing = await getRepository(context.postgres).insertListing(
      // @ts-expect-error to fix
      event.body
    );

    return { statusCode: 201, response: listing };
  }
);

export const updateListing = functionHandler<Listing & ListingReadOnly>(
  async (event, context) => {
    const listing = await getRepository(context.postgres).updateListing(
      parseInt(event.pathParameters.id),
      // @ts-expect-error to fix
      event.body
    );

    return { statusCode: 200, response: listing };
  }
);
