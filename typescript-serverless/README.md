# TypeScript Serverless

Welcome to the TypeScript Serverless version of this test. This README lists the specificities of this application
and how to start developing on this codebase. For more general information about the test, refer to the main README.

This project uses the [Serverless](https://www.serverless.com/) framework to serve the ListingAPI endpoints. We do not
use this framework at AVIV, but chose to use it for this test, so you can experience lambdas development without
needing an AWS account or complex configuration.

## Getting started

To start developing, use the following command:

```
# The image will be built with your user and group id to avoid any
# filesystem permission issue.
export USER_ID=$(id -u)
export GROUP_ID=$(id -g)

docker-compose up typescript-serverless
```

It will start the project and serve the API over the port `8383`. You can then start querying the API.

If you want to run some npm commands, you can do it using the following:

```
# Check the lint of the project
docker-compose run --rm typescript-serverless npm run lint

# Run the tests of the project
docker-compose run --rm typescript-serverless npm run test
```

If you want to install dependencies locally without installing `pg-native` requirements, for instance because you do not have
autocomplete behavior in your IDE, you can use the following command:

```sh
npm install --ignore-scripts
```

## Development

You can find the action you need to implement in `src/functions/price/handler.ts`.

## Known issues

- The library `@serverless/typescript` has some TypeScript errors in the published type definitions. The consequence
  is that when running `tsc` to check the types, you will see an error `Property '"Fn::Transform"' [...] is not assignable
to 'string'`. This is why we use the flag `--skipLibCheck` when checking types in the package.json file. See
  [serverless/typescript](https://github.com/serverless/typescript/issues/27).
- Recent versions of Docker for Mac (> 4.18) [may trigger a segmentation fault](https://github.com/docker/for-mac/issues/6824#issuecomment-1662351336)
  when running the test. If you face the issue, you will need to downgrade to Docker for Mac 4.18.
