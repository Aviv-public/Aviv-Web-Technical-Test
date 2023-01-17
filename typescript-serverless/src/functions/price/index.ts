import { handlerPath } from "@/libs/handler-resolver";
import type { AWSFunction } from "../types";
import { buildEventDefinition } from "@/libs/handler";

export const getListingPriceHistory: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.getListingPriceHistory`,
  events: [{ http: buildEventDefinition("get", "/listings/{id}/history") }],
};
