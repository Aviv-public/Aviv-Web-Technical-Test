# AVIV technical test

Welcome to the AVIV technical test! This README will provide you with everything you need to know to start the exercise.
Please read it thoroughly before you start working on your implementation proposal.

completion time
solution md

## 1. A bit of context

At AVIV, we often deal with _listings_. A listing is the description of a real estate that can be rented or bought. It
contains information such as price and availability. We also display real estates characteristics, such as its category
or size.

It has been decided by the product manager of your team to provide a view of the listings to our customers. Specifically, we want to display
a list of each listing we have in our database, with its price history. Your team has determined that a REST
API should be developed to provide the listings, so they can be displayed on a single page application. Your colleagues developers have
already started to provide a resource endpoint to retrieve, create and update such listings in an API called the
`ListingAPI`.

The `ListingAPI` has a schema that is documented in the [schemas/listingapi.yaml](./schemas/listingapi.yaml) folder.

You should upload the YAML file to [ReDoc](https://redocly.github.io/redoc/) and browse it carefully.

Your team made a schema of the current application architecture
![Application Architecture](./schemas/Aviv-Technical-Test-Architecture.png "Application Architecture")

## 2. Before starting

### Installation

If you need to install Docker Desktop, go to the [Docker Get Started](https://www.docker.com/get-started/) page.
You will also need [`docker-compose`](https://docs.docker.com/compose/) to run this test.

The backend test provides an implementation of the `ListingAPI`.

The frontend test provides an implementation that consumes it.

Before digging into the test, please note the following expectations:

- You should allow about **90 minutes** for this test, including the discovery phase;
- During the development phase, be sure to **write down your assumptions** and any other development you were not able to achieve, in the [SOLUTION.md](./SOLUTION.md) file.

The aim of the technical test is to serve as a basis for the debrief that follows it, in which you will defend your decisions and discuss what might be missing in your implementation.

## 3. The exercise

**If you are applying for a front-end position**, please continue reading the [FRONTEND-README.md](./FRONTEND-README.md) file.

**If you are applying for a back-end position**, please continue reading the [BACKEND-README.md](./BACKEND-README.md) file.

## 4. Deliverable expectations

When you're done, send us a `.zip` file with commits history (keep the `.git` folder). The file should include:

- the `.git/` folder;
- the entire codebase;
- the [SOLUTION.md](./SOLUTION.md) file, with the answers to the questions written above.

If you want to join any additional file, you can add them to the archive and link them in the [SOLUTION.md](./SOLUTION.md) file.
