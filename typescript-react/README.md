# AVIV front-end Test

Welcome to the AVIV front-end test.

This test will assess your skills when working with React. To get started, please read this document carefully, before starting working on the project.

> **⚠️ Heads up!**
> 
> Make sure you have carefully read the [main README file](../README.md) before continuing. It contains _critical_ instructions regarding expectations and test completion.

## Let's get started!

We assume at this point that you read the main README file and are aware of the context of this project, and the test submission modalities.

## Objectives

The aim of this project is to provide in a React application made of two different pages:

- A page that will provide a list of the available listings, with a form to create new ones;
- A page that provides the history of a specific listing.

A bootstrapped project is provided to you with react and some dependencies so you can start working directly without the headache of configuring the project. You will learn on how to run this project later on.

> **ℹ️ Styles and CSS**
> 
> The CSS styling is already provided and that **we don't expect you to focus particularly on that part**. The CSS is built on
[BEM](https://getbem.com/introduction/) principles and can be found in the file [`src/styles/global.scss`](./src/styles/global.scss).

### New listing form

We want the main page to include a form that allows the user to create a new listing. Your objective is to implement that form so new listings are stored in the API when submitted.

(todo link to api spec)

#### Listings Page

We want the main page to provide a list of cards, each card representing a listing. The user should be able to click a card to go to a sub-page that will display the price history of the selected listing.

An [example](./src/containers/Listings/Listings.tsx) of a card is provided along the test for which you have a preview below :

![](./assets/listing-card.png)

#### Listing history page

This sub-page should load and display a simple list of the history for a specific listing.
The sub-page should be accessible through the url `/:listingId/prices`.

### Running the project

You can start developing by running:

```sh
npm run dev
```

To run the tests, you can use:

```sh
npm run test
```

If you need to install additional dependencies, you can of course use the common `npm` commands.

You will need to interact with an API when implementing your front-end. Because we are running in a GitHub Codespace, you will have to use the `BACKEND_API_HOST` environment variable instead of `localhost` to contact this backend. The API is already running.

(todo: explain how to have the API being public)
