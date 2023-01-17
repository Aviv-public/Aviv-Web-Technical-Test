import { APIGatewayProxyEvent, APIGatewayProxyResult } from "aws-lambda";
import PostgresClient from "serverless-postgres";
import { postgres } from "@/libs/postgres";
import middy from "@middy/core";
import middyJsonBodyParser from "@middy/http-json-body-parser";
import { formatJSONResponse } from "./api-gateway";

export type FunctionContext = {
  postgres: PostgresClient;
};

export type FunctionResult<T extends object> = {
  response: T;
  statusCode?: number;
};

export type FunctionHandler<T extends object> = (
  event: APIGatewayProxyEvent,
  context: FunctionContext
) => Promise<FunctionResult<T>>;

function middify(
  handler: (event: APIGatewayProxyEvent) => Promise<APIGatewayProxyResult>
) {
  return middy(handler).use(middyJsonBodyParser());
}

/**
 * Application specific function handler that builds a context and handles
 * database connection and disconnection.
 */
export function functionHandler<T extends object>(handler: FunctionHandler<T>) {
  return middify(
    async (event: APIGatewayProxyEvent): Promise<APIGatewayProxyResult> => {
      await postgres.connect();

      const { response, statusCode } = await handler(event, { postgres });

      await postgres.end();

      return formatJSONResponse(response, statusCode);
    }
  );
}
