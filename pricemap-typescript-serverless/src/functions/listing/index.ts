import { handlerPath } from "@/libs/handler-resolver";
import type { AWSFunction } from "../types";

export const getListings: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.getListings`,
  events: [
    {
      http: {
        method: "GET",
        path: "/listings",
      },
    },
  ],
};

export const addListing: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.addListing`,
  events: [
    {
      http: {
        method: "POST",
        path: "/listings",
      },
    },
  ],
};

export const updateListing: AWSFunction = {
  handler: `${handlerPath(__dirname)}/handler.updateListing`,
  events: [
    {
      http: {
        method: "PUT",
        path: "/listings/{id}",
      },
    },
  ],
};
