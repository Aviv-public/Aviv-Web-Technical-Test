import type { AWS } from "@serverless/typescript";

import { addListing, getListings, updateListing } from "@/functions/listing";
import { getListingPrices } from "@/functions/price";

const serverlessConfiguration: AWS = {
  service: "listingapi",
  frameworkVersion: "3",
  plugins: ["serverless-esbuild", "serverless-offline"],
  provider: {
    name: "aws",
    runtime: "nodejs18.x",
    apiGateway: {
      minimumCompressionSize: 1024,
      shouldStartNameWithService: true,
    },
    environment: {
      AWS_NODEJS_CONNECTION_REUSE_ENABLED: "1",
      NODE_OPTIONS: "--enable-source-maps --stack-trace-limit=1000",
      PGHOST: process.env.PGHOST,
      PGDATABASE: process.env.PGDATABASE,
      PGUSER: process.env.PGUSER,
      PGPASSWORD: process.env.PGPASSWORD,
    },
  },
  // When adding new functions, you need to restart the watcher
  // to reload the configuration.
  functions: { getListings, addListing, updateListing, getListingPrices },
  package: { individually: true },
  custom: {
    esbuild: {
      bundle: true,
      minify: false,
      sourcemap: true,
      exclude: ["aws-sdk"],
      target: "node18",
      define: { "require.resolve": undefined },
      platform: "node",
      concurrency: 10,
    },
  },
};

module.exports = serverlessConfiguration;
