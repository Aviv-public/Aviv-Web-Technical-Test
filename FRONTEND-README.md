# AVIV Front-end Test

[![Aviv logo](./typescript-react/assets/logo-aviv.svg)](https://www.aviv-group.com/)

## Introduction

This repository contains instructions for the Aviv Frontend Technical Test.

Its aim is to give us an overview of your practical technical knowledge through a screening technical test.

## Completion time

There is no critical need to fulfill all the functional and technical requests, so keep in mind to focus on what you
think you can solve within this timeframe rather trying to solve all the demands if this seems out of scope. Quality
over quantity.
If you do not manage to provide all the requested features, please fulfill what are the features missing in
the [SOLUTION.md](../SOLUTION.md) file explaining how you would have provided such feature.

## Objectives

The aim is to provide in a react application two different functional pages :

- A page that will provide a list of the available listings with a form to create new listings.
- A page that will provide the history for a specific listing.

A bootstrapped project is provided to you with react and some dependencies so you can start working directly without the
headache of configuring the project.

### Install

> npm install

### Start the app

> npm run dev

### Launch test :

> npm test

### Design

Note that the CSS styling is already provided and that we don't expect you to focus particularly on that part. The CSS
is built on
[BEM](https://getbem.com/introduction/) principles and can be found in the
file [`src/styles/global.scss`](./src/styles/global.scss).

## Logical and technical expectations

### Listing form

We want the main page to have a form that allows the user to create a new listing.
Below you will find a table of the required fields the user will have to fill in order to be able to submit the form and
be accepted by the server.

### Listings Page

We want the main page to provide a list of cards, each card representing a listing. The user should be able to click a
card to go to a sub-page that will display the price history of the selected listing.

An [example](./typescript-react/src/components/ListingCard/ListingCard.tsx) of a card is provided along the test for which you have a preview
below :

<img src="./typescript-react/assets/listing-card.png"  width="400">

### Listing history page

This sub-page should load and display a simple list of the history for a specific listing.
The sub-page should be accessible through the url `/:listingId/prices`.

## How to start the test

Simply clone the repository :

> git clone git@github.com:MeilleursAgents/aviv-technical-test.git

## Docker API

### Installation

To start the API you will need to install Docker Desktop first , go to [Docker](https://www.docker.com/get-started).

### Start the API

The [Swagger](https://swagger.io/solutions/api-documentation/) and API are available at the following
address http://localhost:8080 by using the command from the root folder:

> make python-run

### API Endpoints

The API will provide you with the data you need in order to produce the expected rendering.

- GET - List of listings:

  > http://localhost:8080/listings

  Response samples:

  ```ts
  [
      {
          "id": 1,
          "bedrooms_count": 2,
          "building_type": "STUDIO",
          "contact_phone_number": "+219779210354",
          "created_date": "2023-01-17T14:19:22.808738",
          "description": "",
          "latest_price_eur": 710000.0,
          "name": "Mikhail Schmiedt",
          "postal_address": {
              "city": "Berchtesgaden",
              "country": "DE",
              "postal_code": "21810",
              "street_address": "Johan-Ernst-Ring 7"
          },
          "rooms_count": 6,
          "surface_area_m2": 167.0,
          "updated_date": "2023-01-17T14:20:47.707666"
      },
      /* ... */
      {
          "id": 100,
          /* ... */
      }
  ]
  ```

- GET - Prices history of a specific listing:

  > http://localhost:8080/listings/{id}/prices

  Path Parameters (REQUIRED):

  ```ts
    id: string //The id for the listing to get price history from.
  ```

  Response samples:

    ```ts
    [
        {
            "created_date": "2023-01-12T09:23:36Z",
            "price_eur": 100000
        },
        {
            "created_date": "2023-01-17T08:17:32Z",
            "price_eur": 150000
        },
        /* ... */
    ]
    ```

- POST - Create a new listing:

  > http://localhost:8080/listings

  Request body schema (all fields are REQUIRED):

  ```
    bedrooms_count: NUMBER, //The number of bedrooms
    building_type: STRING  //The type of building the listing referers to. allowed values : STUDIO, APARTMENT, HOUSE.
    contact_phone_number: STRING //Listing main contact phone number, following the E.164 standard. Match patten : ^\+[1-9]\d{1,14}$.
    description: STRING  //A user friendly description for the listing.
    latest_price_eur: NUMBER  //The price of the listing, in euros.	
    name: STRING //A user friendly name for the listing.
    postal_address: {
        street_address: STRING //The street address of the postal address.	
        postal_code: STRING //The postal code of the postal address.	
        city: STRING //The city of the postal address.	
        country: STRING //The country of the Postal Address, as a ISO 3166-1 alpha-2 country code.	
        }
    rooms_count: NUMBER //The number of rooms of the listing.
    surface_area_m2: NUMBER  //The surface of the listing, in square meters.
  ```

  Payload example:

    ```ts
    {
    "bedrooms_count": 2,
    "building_type": "STUDIO",
    "contact_phone_number": "+219779210354",
    "description": "description",
    "latest_price_eur": 710000.0,
    "name": "Mikhail Schmiedt",
    "postal_address": {
      "city": "Berchtesgaden",
      "country": "DE",
      "postal_code": "21810",
      "street_address": "Johan-Ernst-Ring 7"
    },
    "rooms_count": 6,
    "surface_area_m2": 167.0
  }
  
    ```

  Response samples:

    ```ts
    {
    "id": 1,
    "bedrooms_count": 2,
    "building_type": "STUDIO",
    "contact_phone_number": "+219779210354",
    "created_date": "2023-01-17T14:19:22.808738",
    "description": "",
    "latest_price_eur": 710000.0,
    "name": "Mikhail Schmiedt",
    "postal_address": {
      "city": "Berchtesgaden",
      "country": "DE",
      "postal_code": "21810",
      "street_address": "Johan-Ernst-Ring 7"
    },
    "rooms_count": 6,
    "surface_area_m2": 167.0,
    "updated_date": "2023-01-17T14:20:47.707666"
  }
    ```

Note that you can also access the endpoint documentation following [the context section](./BACKEND-README.md#context) of
the
main README.


