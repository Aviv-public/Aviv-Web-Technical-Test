import { HttpEventHandler } from "@/functions/types";
import { getRequestBodySchema } from "@/openapi";

export function buildEventDefinition(
  method: string,
  path: string
): HttpEventHandler {
  const eventDefinition: HttpEventHandler = {
    method,
    path,
  };

  if (["post", "put"].includes(method)) {
    eventDefinition.request = {
      schemas: {
        "application/json": getRequestBodySchema(method, path),
      },
    };
  }

  return eventDefinition;
}
