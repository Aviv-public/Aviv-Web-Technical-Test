import { handlerPath } from "@/libs/handler-resolver";
import type { AWSFunction } from "../types";

export const getListingPriceHistory: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.getListingPriceHistory`,
  events: [
    {
      http: {
        method: "GET",
        path: "/listings/{id}/history",
      },
    },
  ],
};
