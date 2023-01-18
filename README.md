# AVIV technical test

This repository contains the technical test that you are expected to fulfill. It contains multiple folders, depending
on the position you applied to.

## Prerequisites

All those tests provide an implementation of a similar REST API, and a front-end consuming it. Before digging into
this API, please note the following expectations:

- The test is expected to be **achieved in 90 minutes**, including the discovery phase;
- You are expected to work in **one of the available codebase** depending on the position you applied to;
- During the development phase, be sure to **write down your assumptions** and any other development you were not
  able to achieve, in the [SOLUTION.md](./SOLUTION.md) file.

The aim of the technical is to serve as a base for a debrief, in which you will defend your choices, and discuss what is
missing in your implementation.

You can find the instructions on how to hand over your solution in the [SOLUTION.md](./SOLUTION.md) file.

## Context

At AVIV, we often deal with _listings_. A listing is the description of a real estate that can be rented or bought. It
contains information such as price and availability. We also display real estates characteristics, such as its category
or size.

Your objective is to work with a REST API, the ListingsAPI, to display listings and their price history (for the front-end
test) or to write down the code to serve the price history of a given listing (for the back-end test).

The ListingsAPI has a schema that is documented in the [schemas/listingsapi.yaml](./schemas/listingsapi.yaml) folder.

### Front-end test

If you applied to a front-end position, you can continue by reading the README.md in the front-end test directory.

### Back-end test

If you applied to a back-end position, you can continue by reading the README.md in the back-end test directory of the
language of your choice. You have several flavors available:
- Python
- TypeScript
- C#
