import { functionHandler } from "@/libs/function";
import { Price } from "@/types.generated";

export const getListingPrices = functionHandler<Price[]>(async () => {
  // Replace this with your implementation.
  return {
    statusCode: 200,
    response: [
      { price_eur: 100000, created_date: "2023-01-12T09:23:36Z" },
      { price_eur: 150000, created_date: "2023-01-17T08:17:32Z" },
    ],
  };
});
