import { AWS } from "@serverless/typescript";

export type AWSFunction = AWS["functions"]["Function"];
export type HttpEventHandler = Extract<
  Extract<AWSFunction["events"][0], { http: unknown }>["http"],
  object
>;
