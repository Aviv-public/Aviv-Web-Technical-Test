# AVIV technical test

Welcome to the AVIV technical test! This README will provide you with everything you need to know to start the exercise.
Please read it thoroughly before starting working on your implementation proposal.

## 1. A bit of context

At AVIV, we often deal with _listings_. A listing is the description of a real estate that can be rented or bought. It
contains information such as price and availability. We also display real estates characteristics, such as its category
or size.

It has been decided by the product team to provide a view of our listings to our customer. Specifically, we want to display
a list of each listing we have in our database, with its price history. The technical team, has determined that a REST
API should be developed to provide the listings, so they can be displayed on a single page application. Developers have
already started to provide a resource endpoint to retrieve, create and update such listings in an API called the
`ListingAPI`.

The ListingAPI has a schema that is documented in the [schemas/listingapi.yaml](./schemas/listingapi.yaml) folder.

You should upload the YAML file to [ReDoc](https://redocly.github.io/redoc/) and browse it carefully.

## 2. Before starting

You will need [`Docker`](https://www.docker.com/) and [`docker-compose`](https://docs.docker.com/compose/) to run this test.

All backend tests provide an implementation of the `ListingAPI`. The front-end test provides an implementation that
consumes it. Before digging into the test, please note the following expectations:

- You shall allocate around **90 minutes** on this test, including the discovery phase;
- During the development phase, be sure to **write down your assumptions** and any other development you were not
  able to achieve, in the [SOLUTION.md](./SOLUTION.md) file.

The aim of the technical is to serve as a base for a debrief, in which you will defend your choices, and discuss what is
missing in your implementation.

## 3. The exercise

**If you are applying for a front-end position**, please take a look on the [FRONTEND-README.md](./FRONTEND-README.md) file

**If you are applying for a back-end position**, please take a look on the [BACKEND-README.md](./BACKEND-README.md) file

## 4. Render Expectation

Send us a `.zip` file with commits history (keep the `.git` folder). The file should include:
- the `.git/` folder;
- the entire codebase;
- the [SOLUTION.md](./SOLUTION.md) file, with the answers to the questions written above.

If you want to join any additional file, you can add them to the archive and link them in
the [SOLUTION.md](./SOLUTION.md) file.
