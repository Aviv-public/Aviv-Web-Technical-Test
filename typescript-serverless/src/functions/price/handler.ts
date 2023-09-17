import { functionHandler } from "@/libs/function";
import { Price } from "@/types.generated";
import { EntityNotFound, NotFound } from "@/libs/errors";
import { getPriceRepository } from "@/repositories/prices";

export const getListingPrices = functionHandler<Price[]>(
  async (event, context) => {
    try {
      const prices = await getPriceRepository(context.postgres).getPrices(
        parseInt(event.pathParameters.id)
      );

      return {
        statusCode: 200,
        response: prices,
      };
    } catch (e) {
      if (e instanceof EntityNotFound) {
        throw new NotFound(e.message);
      }

      throw e;
    }
  }
);
