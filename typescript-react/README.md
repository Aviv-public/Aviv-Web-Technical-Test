**Welcome to the AVIV front-end test.**

This test will assess your skills when working with React. To get started, please read this document carefully, before starting working on the project.

> **⚠️ Heads up!**
> 
> Make sure you have carefully read the [main README file](../README.md) before continuing. It contains _critical_ instructions regarding expectations and test completion.

# Objectives

The aim of this project is to provide in a React application made of two different pages:

- A page that will provide a list of the available listings, with a form to create new ones;
- A page that provides the history of a specific listing.

To achieve this, you will need to complete multiple objectives.

## Objective 1: New listing form

We want the main page to include a form that allows the user to create a new listing. Your objective is to implement that form, so new listings are stored in the API when submitted.

## Objective 2: Listings Page

We want the main page to provide a list of cards, each card representing a listing. The user should be able to click a card to go to a sub-page that will display the price history of the selected listing.

An [example](./src/containers/Listings/Listings.tsx) of a card is provided along the test for which you have a preview [here](./assets/listing-card.png).

## Objective 3: Listing price history page

This sub-page should load and display a simple list of the price history for a specific listing.
The sub-page should be accessible through the URL `/:listingId/prices`.

## Objective 4: Answer the questions in the pull request

When you will create the pull request to hand over your work, it will contain a few questions. Do not forget to plan for some time to answer all of them. You can 
read more about it in the [main README file](../README.md#iii---handing-over-your-work).

> **ℹ️ Styles and CSS**
> 
> The CSS styling is already provided, and **we do not expect you to focus particularly on that part**. The CSS is built on
[BEM](https://getbem.com/introduction/) principles and can be found in the file [`src/styles/global.scss`](./src/styles/global.scss).

# Running the project

A bootstrapped project is provided to you with React and some dependencies, so you can start working directly without the headache of configuring the project.

## Browsing the API

You will need to interact with an API when implementing your front-end. Because we are running in a GitHub Codespace, you will have to use the `VITE_BACKEND_API_HOST` environment variable instead of `localhost` to connect to this backend. The API is already running. Here is an example command to get the list of listings:

```sh
echo https://${VITE_BACKEND_API_HOST}/listings
curl https://${VITE_BACKEND_API_HOST}/listings
```

The variable is pre-populated in the Codespace. You can read more on how to use it in the `.env` file.

This API is described by an OpenAPI specification. You can open and view this specification in ReDoc by using the terminal and running the following command:

```sh
echo ${REDOC_URL}
```

Click on the displayed URL and browse the documentation to understand how the API works. If you are having trouble to get it work, you can also download
the OpenAPI schema in the `schemas/listingapi.yaml` file (from GitHub).

## Beginning development

You can start developing by running the following command, and reading the warning carefully:

```sh
npm run dev
```

> **⚠️ How can I access my development server?**
> 
> The output displays that the development servers is running on `localhost`. Of course, because you are using a GitHub Codespace, you cannot access this URL directly, because it would point to your local machine. However, if you `ctrl`+`click` on it, GitHub Codespace will automatically substitute `localhost` so it points to the cloud running instance. You can see all running services in the `PORTS` tab on the bottom panel of this IDE.

To run the tests, you can use:

```sh
npm run test
```

If you need to install additional dependencies, you can of course use the usual `npm` commands.

**Good luck**, and do not forget to read again the [main README file](../README.md) to ensure you did not forget anything when you think you're done!
