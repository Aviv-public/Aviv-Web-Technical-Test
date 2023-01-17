import { buildEventDefinition } from "@/libs/handler";
import { handlerPath } from "@/libs/handler-resolver";
import type { AWSFunction } from "../types";

export const getListings: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.getListings`,
  events: [{ http: buildEventDefinition("get", "/listings") }],
};

export const addListing: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.addListing`,
  events: [{ http: buildEventDefinition("post", "/listings") }],
};

export const updateListing: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.updateListing`,
  events: [{ http: buildEventDefinition("put", "/listings/{id}") }],
};
