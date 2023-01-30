## Back-end exercice

### Context
Your team has created the ListingAPI, that handles listings.
Today, you have picked a ticket in the Kanban and need to implement
a **new feature** to persist price changes for a given listing over time.

### Structure

The ListingAPI has a schema that is documented in the [schemas/listingapi.yaml](./schemas/listingapi.yaml) folder.

Note that you can upload the YAML file to [ReDoc](https://redocly.github.io/redoc/) to read it comfortably.
Your team also prepared a Postman collection to easily interact with the API.
It is available on the [Schemas directory](./schemas/postman).
You can import it directly and run

The Listing API exposes 4 endpoints : 

#### GET /listings

This endpoint will get from the database all persisted listings

```http request
GET /listings

{
    ...
    "latest_price_eur": 100000
    ...
}
```

#### POST /listings

This endpoint allow us to create a new listing : 

```http request
POST /listings

{
    ...
    "latest_price_eur": 100000
    ...
}
```

On this example, a listing is created using the API, with a specified price `100000`


#### PUT /listings/<id>

This endpoint allow us to update a listing for a given ID `<id>`

```http request
PUT /listings/<id>

{
    ...
    "latest_price_eur": 150000
    ...
}
```

On this example, the listing is updated using the API, with a new price `150000` 📈

#### GET /listings/<id>/prices

This endpoint will retrieve all prices changes for a given listing ID `<id>`

```

[
    { "price_eur": 100000, "created_date": "2023-01-12T09:23:36Z" },
    { "price_eur": 150000, "created_date": "2023-01-17T08:17:32Z" },
]
```

### The Exercice

The [endpoint that returns listing price changes](#get-listings-id-prices) returns mocked data. 

**You are expected to store the listing prices history and return it instead of the mocked response.**

### Back-end versions

The test is declined in 3 versions
- [Python Flask](./python-flask)
- [TypeScript Serverless](./typescript-serverless)
- [C# .NET](./c#-dotnet)

You can continue by reading the README.md in the back-end test directory of the language of your choice.

**You must pick the one that is relevant to the position your applying to.**
