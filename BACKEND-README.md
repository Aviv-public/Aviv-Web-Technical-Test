## Back-end exercice

### Context
We have create an API to handle listings. 
Today we need to implement a **new feature to persist** price changes over the time for a listing. 

### Structure

The ListingAPI has a schema that is documented in the [schemas/listingapi.yaml](./schemas/listingapi.yaml) folder.

Note that you can upload the YAML file to [ReDoc](https://redocly.github.io/redoc/) to read it comfortably.
Otherwise, Postman collection is available on the [Schemas directory](./schemas/postman). You can import it directly and run
API calls by choosing your environment (`Python Flask`, `C# .NET` or `Typescript Serverless`).

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
    "latest_price_eur": 200000
    ...
}
```

On this example, the listing is updated using the API, with a new price `200000` 📈

#### GET /listings/<id>/prices

This endpoint will retrieve all prices changes for a given listing ID `<id>`
```

[
    { price_eur: 100000, created_date: "<creation date>" },
    { price_eur: 200000, created_date: "<first update date>" },
    { price_eur: 175000, created_date: "<second update date>" }
]
```

### The Exercice

The [endpoint that returns listing price changes](#get-listings-id-prices) returns mocked data. 

**We expect from you to implement a way to replace those mocked data by real ones**

### Back-end versions

The test is declined in 3 versions
- [Python Flask](./python-flask)
- [TypeScript Serverless](./typescript-serverless)
- [C# .NET](./c#-dotnet)

You can continue by reading the README.md in the back-end test directory of the language of your choice.

**You must pick the one that is relevant to the position your applying to.**
