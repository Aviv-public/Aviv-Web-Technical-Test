# Backend technical test: Price map in Paris

The objective is to build a price map of the average selling prices (€/m²) per arrondissement (district) in Paris, with statistics, from an API of listings from MeilleursAgents.

Here is an example of what we want to achieve:

![image 2](pricemap/img/image2.png)
![image 1](pricemap/img/image1.png)

A part of the project is already completed. To make it work, the following tools are required:
- `docker`
- `docker-compose`
- `make`

For the rest, you can use the tools you prefer.

The following features are already set up:
- a web application for visualization (`pricemap`)
- a database (`PostgreSQL`)
- a real estate properties API of listings for Paris (`listingapi`)
- a first implementation for the part 1 ("Collecting data") and the part 2 ("Displaying prices")

**The entirety of your code must run in the `pricemap` container.**

A documentation detailing how the project is designed can be found [here](./usages.md) to understand how to start the project, interact and enter into containers if needed, ...

## 1 - Collecting data

We want to collect the entirety of real estate properties in Paris. These properties will be retrieved from the real estate properties API (`listingapi`), that you will need to browse entirely.

**You must not change the `listingapi`, it only serves at exposing data.**

You can access this API, after starting the project :
- from your local environment, at: http://localhost:8181/listings/32682
- from the container of your `pricemap` application at: http://listingapi:5000/listings/32682

To get started, a first implementation already exists in the `app.py` file. This code adds a `/update_data` endpoint to the `pricemap` app, which starts data retrieval.

**This code does work, but requires improvements.**

The aim of this part is to rework and complete existing code, to make it cleaner, easier to maintain and to match the state of the art.
You can work the way you want, you can move code, add libraries, change the way code is called, etc.

#### 1.1 -  Location filter

In Paris, we want to display listings per arrondissement.

When calling the `listingapi`, the parameter of the request named `place_id` will successively take the value of each Paris arrondissement identifier as presented in the following array.

Those identifiers are also available in database, in the public schema in a table called `geo_place`, containing Paris arrondissements and their COG (Code Officiel Géographique - official geographical code).

| Arrondissement | Id |
| ------- | ----------|
| Paris 1 | 32682 |
| Paris 2 | 32683 |
| Paris 3 | 32684 |
| Paris 4 | 32685 |
| Paris 5 | 32686 |
| Paris 6 | 32687 |
| Paris 7 | 32688 |
| Paris 8 | 32689 |
| Paris 9 | 32690|
| Paris 10 | 32691 |
| Paris 11 | 32692 |
| Paris 12 | 32693 |
| Paris 13 | 32694 |
| Paris 14 | 32695 |
| Paris 15 | 32696 |
| Paris 16 | 32697 |
| Paris 17 | 32698 |
| Paris 18 | 32699 |
| Paris 19 | 32700 |
| Paris 20 | 32701 |


#### 1.2 - Pagination

The `listingapi` sends pages of 20 listings. You will have to browse all pages for all arrondissements, using the parameter `?page=<page_number>`.

Example: http://listingapi:5000/listings/32682?page=7

The number of pages is different for each arrondissement: from zero to dozens of pages. You will have to imagine a mechanism that can be adapted to the number of pages to browse. There are multiple implementations possible.

### 1.3 Extracting listings properties

For each listing, we are interested in the following properties:
- `listing_id`: listing identifier for MeilleursAgents;
- `place_id`: arrondissement identifier (as passed in the query parameters);
- `price`: selling price, integer, euros;
- `area`: area, integer, square meters;
- `room_count`: number of rooms, integer.

It is possible that some properties might not be exposed as expected by the `listingapi` API, and that some of those might require to be extracted. Beware of the 1-room apartments called « Studio ».

### 1.4 - Data structure in database

Once listings are extracted, following above specification, they must be stored in a database, in one or multiple tables. The existing code implementation stores listings in a `listings` table.
As told before, you can adjust data modeling if needed.

In addition to their properties, we also want to model the evolution of listings across time. Concretely, we want to know:
- when the listing was put online (or at least when it was seen for the first time)
- when the listing was removed (or when we saw it for the last time)
- the full price history

Here are the required credentials to connect to the database:

- type : PostgreSQL (module `psycopg2` en Python)
- host : `db`
- port: `5432`
- user : `pricemap`
- password : `pricemap`
- database : `pricemap`

## 2 - Displaying prices

The map and the histogram presented in the introduction of this document are served by a web application written in Python, using Flask micro-frontend.

As for part 1, the web application is already working, but **can be improved**.

### 2.1 - Displaying prices for each arrondissement

When the page loads, the JavaScript code that generates the map calls the Python web application to get the list of geographical entities to display. The web application responds with GeoJSON formatted data that contains a list of arrondissements to display, their geometrical shape as well as an average price. The color of the shape depends on the price of the arrondissement that is represented, following the same color scale as the one currently used on MeilleursAgents website for Paris map.

For each arrondissement, the average price per real square meter is computed, to be displayed on the website.

Code is already implemented in the `/geoms` endpoint in `pricemap/pricemap/blueprints/api.py`. As for the first part of this exercise, code does work but can be improved: by checking the calculation, improving the SQL request, improving data modeling, etc.

### 2.2 - Displaying stats for each arrondissement

When we click on an arrondissement, an histogram is displayed. It represents the listings' distribution per price bin for this arrondissement. As previously, JavaScript code in charge of generating this histogram asks the web application before each display, by passing the arrondissement identifier as a query parameter. The web application responds with JSON formatted data that contains, among others, the values for each bar of the histogram. The y-axis is then automatically scaled based on the returned values.

For each targeted arrondissement, the listings price distribution is calculated on the API side, to be integrated to the response of the web application. The JavaScript code will use this response to generate the histogram.

Code is already implemented in the `/get_price/<path:cog>` endpoint in `pricemap/pricemap/blueprints/api.py`. As for the other endpoint, code can be improved. You can change distribution, labels, calculation method of the histogram, etc.

### 2.3 - Displaying the average price of the arrondissement (bonus)

Between the map and the histogram, we never display the average price of the arrondissement in as a number. What could we do to display it on the web page when we click on an arrondissement on the map?

## 3 - Industrialization

### 3.1 - Scaling

We now want to have price history at France scale to offer a price map containing values as recent as possible to the users of our public website.

To do so, you need to think about an architecture that will fulfill the following constraints:

1. Inserting listings prices for France in less than 5 minutes
2. Guarantee a <500ms response time when consulting the map, independently of the number of users currently connected

You have all the money you want, can use any tool, language, framework, infrastructure.

The expected output of your study is a schema (you can for instance use https://draw.io) that will be used as a base for discussion during the debrief.
