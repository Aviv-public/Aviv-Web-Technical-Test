# TypeScript Serverless

Welcome to the TypeScript Serverless version of this test. This README lists the specificities of this application
and how to start developing on this codebase. For more general information about the test, refer to the main README.

This project uses the [Serverless](https://www.serverless.com/) framework to serve the ListingsAPI endpoints.

## Getting started

To start developing, use the following command: 

```
docker-compose up typescript-serverless
```

It will start the project and serve the API over the port `8383`. You can then start querying the API.

If you want to run some npm commands, you can do it using the following:

```
# Check the lint of the project
docker-compose typescript-serverless npm run lint

# Run the tests of the project
docker-compose typescript-serverless npm run test
```

If you want to install dependencies locally without installing `pg-native` requirements, for instance because you do not have
autocomplete behavior in your IDE, you can use the following command:

```sh
npm install --ignore-scripts
```

## Development

You can find the action you need to implement in `src/functions/price/handler.ts`.

