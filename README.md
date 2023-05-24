# AVIV technical test

Welcome to the AVIV technical test! This README will provide you with everything you need to know to start the exercise.
**Please read it thoroughly before you start working on your implementation proposal.**

![AVIV logo](./docs/aviv-logo.svg)

## Before you start

**Pick the right test.** You are expected to achieve *one* technical test to assert your technical skills depending on the interview process you are currently in. If you are unsure of which test you should achieve, please reach out to the recruiter you are in contact with.

**Spend a reasonable amount of time.** There is no hard limit on how much time you should spend on the exercise. In practice, we do not expect candidates
to spend more than three hours on it. In the pull request you will create, a few questions will be asked, including the amount of time you spent on it.

**Running the test.** We recommend candidates to use GitHub Codespaces to run this test. It is preconfigured so you can start to code quickly, enabling you
to show most of your skills. You can still clone the repository and work locally if you prefer. Note that you can also work in a hybrid environment, using
a local IDE while having your code running remotely. It comes with a few drawbacks documented in the [Known issues](#known-issues) section below.

## Getting started

Please follow carefully these instructions to get started. This is the recommended path to run the technical test and should save you plenty of setup times.
You can always chose a different approach you are more used to (e.g., cloning and running locally the test), at the risk of spending more time on the test.

### I - Create your Codespace

GitHub provides a feature called GitHub Codespaces to allow developing using VS Code directly in development containers. This is the recommended approach for
completing this test.

1. Click on the green `‹› Code` button at the top of this page.
2. Click on `⋯` at the top right of the modal. ⚠️ Make sure to *not* use the big green `Create codespace` button.
3. Click on `+ New with options...`.
4. In the `Dev container configuration`, choose the one that matches the technical test you're expected to perform. ⚠️ Do not change the branch on the new page nor the region or the Machine type.
5. Click on the `Create codespace` button.

Creating the Codespace can take a few minutes. Read the following steps while waiting.

> **⚠️ Heads up!**
> 
> Before starting using your Codespace, **please finish reading the following**.

### II - A few tips on how to use a Codespace

When the Codespace, please wait a few additional seconds. The Codespace is ready when the README is opened and displayed in the main screen of VS Code. You may
not see a loader while it's getting prepared. Just be patient. You can assume the Codespace is ready when the README is displayed to you.

By default, the Codespace will be pre-configured so you can immediately start coding. The port forwarding rules are pre-configured so you do not have to perform
any additional configuration. If you are unsure on how to reach a service from your Codespace, you can go to the `PORTS` tab next to your console. You will see
all the services. Services that do not have a green dot are not started yet. You will launch them by following the Codespace README.

You can click on the local address to access the running service (e.g., a running API). By default, the visibility of services is private (it means you need to
be authenticated with GitHub to load the page). If you want access from an exernal tool (for instance Postman), you can change the visibility to Public.

You can use Git normally in your Codespace.

### III - Handing over your work

When you have completed the exercises, you are expected to send a pull request link to the recruiter. Make sure to read and answer the questions in the
pull request template, and provide all the relevant details. This pull request will be reviewed by multiple developers from AVIV. If you want to have
a look at the questions you are expected to answer to manage your time properly, you can have a look to the [pull request template](./.github/pull_request_template.md).

### IV - A bit of context

At AVIV, we often deal with _listings_. A listing is the description of a real estate that can be rented or bought. It
contains information such as price and availability. We also display real estates characteristics, such as its category
or size.

It has been decided by the product manager of your team to provide a view of the listings to our customers. Specifically, we want to display
a list of each listing we have in our database, with its price history. Your team has determined that a REST
API should be developed to provide the listings, so they can be displayed on a single page application. Your colleagues developers have
already started to provide a resource endpoint to retrieve, create and update such listings in an API called the
`ListingAPI`.

Your team made a schema of the current application architecture:

![Application Architecture](./docs/Aviv-Technical-Test-Architecture.png "Application Architecture")

### V - You can start coding!

You can now start reading the README in your Codespace. Enjoy coding!

## Known issues

This section contains a few details on known issues and workarounds.

### Working with JetBrains Gateway

JetBrains provides a beta software called Gateway, allowing to work with Codespaces while having your IDE running locally. It can starve your Codespace as it
requires a Java connector to run in the Codespace. In practice, we advise to either increase the CPU and RAM of your Codespace (at the risk of burning your free
credit faster) or go with VS Code for this test. We do not provide support for using JetBrains for this test (but teams are relying a lot on JetBrains awesome 
products at AVIV).
