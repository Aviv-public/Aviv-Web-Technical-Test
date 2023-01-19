# AVIV technical test

This repository contains the technical test that you are expected to fulfill. It contains multiple folders, depending
on the position you applied to.

## Context

At AVIV, we often deal with _listings_. A listing is the description of a real estate that can be rented or bought. It
contains information such as price and availability. We also display real estates characteristics, such as its category
or size.

It has been decided by the product team to provide a view of our listings to our customer. Specifically, we want to display
a list of each listing we have in our database, with its price history. The technical team, has determined that a REST
API should be developed to provide the listings, so they can be displayed on a single page application. Developers have
already started to provide a resource endpoint to retrieve, create and update such listings in an API called the
`ListingsAPI`.

The ListingsAPI has a schema that is documented in the [schemas/listingsapi.yaml](./schemas/listingsapi.yaml) folder.

Note that you can upload the YAML file to [ReDoc](https://redocly.github.io/redoc/) to read it comfortably.

## Prerequisites

You will need `Docker` and `docker-compose` to run this test.

All backend tests provide an implementation of the `ListingsAPI`. The front-end test provides an implementation that
consumes it. Before digging into the test, please note the following expectations:

- You shall allocate around **90 minutes** on this test, including the discovery phase;
- During the development phase, be sure to **write down your assumptions** and any other development you were not
  able to achieve, in the [SOLUTION.md](./SOLUTION.md) file.

The aim of the technical is to serve as a base for a debrief, in which you will defend your choices, and discuss what is
missing in your implementation.

You can find the instructions on how to hand over your solution in the [SOLUTION.md](./SOLUTION.md) file.

## Functional expectations

### Front-end expectations

**If you applied to a front-end position**, you can continue by reading the README.md in the front-end test directory.

### Back-end expectations

**If applied to a backend position**, you are expected to write the code, so we can, for a specific listing,
see all the prices that was given to it.

A Postman collection is available on the [Schemas directory](./schemas/postman). You can import it directly and run
API calls by choosing your environment (`Python Flask`, `C# .NET` or `Typescript Serverless`).

For instance, you can consider this simple scenario:

- a listing is created using the API, with a specified price `100000`

```
POST /listings

{
    ...
    "latest_price_eur": 100000
    ...
}
```

- a listing is updated using the API, with a new price `200000`

```
PUT /listings/<id>

{
    ...
    "latest_price_eur": 200000
    ...
}
```

- when trying to retrieve the prices for this specific listing, we should see two prices listed

```
GET /listings/<id>/prices

[
    { price_eur: 100000, created_date: "<creation date>" },
    { price_eur: 200000, created_date: "<update date>" }
]
```

You can continue by reading the README.md in the back-end test directory of the language of your choice.

You have several flavors available:
- [Python Flask](./python-flask/README.md)
- [TypeScript Serverless](./typescript-serverless)
- C# .NET

You must pick the one that is relevant to the position your applying to.
