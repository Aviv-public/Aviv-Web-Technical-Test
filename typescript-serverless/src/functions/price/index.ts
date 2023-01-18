import { handlerPath } from "@/libs/handler-resolver";
import type { AWSFunction } from "../types";
import { buildEventDefinition } from "@/libs/handler";

export const getListingPrices: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.getListingPrices`,
  events: [{ http: buildEventDefinition("get", "/listings/{id}/prices") }],
};
