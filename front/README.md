# AVIV Owner Front-end Test

## Introduction

This repository contains instructions for the Aviv - Owner - Frontend Technical Test.

Its aim is to give us an overview of your practical technical knowledge through a screening technical test.

## Completion time

This test is designed to get completed in a 30 to 60 minutes timeframe.

There is no critical need to fulfill all the functional and technical requests, so keep in mind to focus on what you think you can solve within this timeframe rather trying to solve all the demands if this seems out of scope. Quality over quantity.

## Install

Yarn : 
> yarn install

Npm:
 > npm i

## Run
Yarn :
> yarn dev

npm : 
> npm start

## Launch test : 

Yarn:
> yarn test

Npm:
> npm test

## Objectives

The aim is to provide in a react application two different functional pages : 
- A page that will provide a list of the available listings 
- A page that will provide the history for a specific listing

Note that the CSS styling is already provided and that we don't expect you to focus particularly on that part.

## Logical and technical expectations 

**Product functionalities:**
- I can see a list of available listings on the main page of the application
- I can go to the detail of the history of a specific listing by clicking onto an element of the list
- I can go directly to a specific list page through the URL `/:listingId`

**Technical** 
- The code is unit tested
- The code is e2e tested



## How to start the test

This repository being a template, it's possible to create a new project using this one as a template. Check the big green Template button. Thanks to let the generated project as a private one.

Alternatively, you can always clone this repository.

> git clone git@github.com:MeilleursAgents/frontend-technical-test.git


## API Endpoints

The API will provide you with the data you need in order to produce the expected rendering. 

- List of listings: 
> curl http://localhost:8080/listings/history

- History of a specific listing:
> curl http://localhost:8080/listings/:listingId/history

## Data sample
Below is an example of listing with history that will be provided by the API : 
```json
{
    "id": 1969719989,
    "place_id": 32684,
    "area": 19,
    "room_count": 1,
    "seen_at": "2023-01-03 16:10:34.117743",
    "history" : [
        {
            "date": "2022-12-01 10:00:00",
            "price": 295000,
        },
        {
            "date": "2022-11-01 10:00:00",
            "price": 293000,
        },
        {
            "date": "2022-10-01 10:00:00",
            "price": 290000,
        }
    ]
  }
```