## Back-end exercise

### Context

Your team has created the `ListingAPI`, that handles listings.
Today, you have picked a ticket in the Kanban and need to implement
a **new endpoint**  that will return the price changes for a given listing over time.

### API structure

The `ListingAPI` has a schema that is documented in the [schemas/listingapi.yaml](./schemas/listingapi.yaml) folder.

Note that you should upload the YAML file to [ReDoc](https://redocly.github.io/redoc/) to read it comfortably.
Your team also prepared a Postman collection to easily interact with the API.
It is available on the [Schemas directory](./schemas/postman).
You can import it directly and run
API calls by choosing your environment (`Python Flask`, `C# .NET` or `Typescript Serverless`).

The `ListingAPI` exposes 4 endpoints : 

#### GET /listings

This endpoint will return all persisted listings.

```http request
GET /listings

[
    {
        ...
        "latest_price_eur": 100000
        ...
    }
]
```

On this example, the API has a single persisted listing.

#### POST /listings

This endpoint will persist a new listing and return it.

```http request
POST /listings

{
    ...
    "latest_price_eur": 100000
    ...
}
```

On this example, a listing is created using the API, with a specified price: `100000`.

#### PUT /listings/\<id\>

This endpoint will update a persisted listing described by its identifier `<id>`.

```http request
PUT /listings/<id>

{
    ...
    "latest_price_eur": 150000
    ...
}
```

On this example, the listing is updated using the API, with a new price: `150000`.

#### GET /listings/\<id\>/prices

This endpoint will return all prices changes for a persisted listing described by its identifier `<id>`.

```
[
    { "price_eur": 100000, "created_date": "2023-01-12T09:23:36Z" },
    { "price_eur": 150000, "created_date": "2023-01-17T08:17:32Z" },
]
```

On this example, there are two prices in the listing history. If the listing is updated with a new
price, a third price should appear in this list, with the date of the update.

### The exercise

The [endpoint that returns listing price changes](#get-listings-id-prices) returns mocked data. 

**You are expected to store the listing prices history and return it instead of the mocked response.**

```gherkin
Given a listing has been created with an initial price of 100 000€ on the 2023/01/12, 09:23:36
When I update the listing with a new price of 150 000€ on the 2023/01/17, 08:17:32
Then the listing prices history for this listing should be as follow:
"""
- date: 2023/01/12, 09:23:36 ; price: 100 000€ 
- date: 2023/01/17, 08:17:32 ; price: 150 000€
"""
When I update the listing again with a new price of 125 000€ on the 2023/01/21, 18:37:14
Then the listing prices history for this listing should be as follow:
"""
- date: 2023/01/12, 09:23:36 ; price: 100 000€
- date: 2023/01/17, 08:17:32 ; price: 150 000€
- date: 2023/01/21, 18:37:14 ; price: 125 000€
"""
```

Any price change should be appended to the list.

### Back-end versions

The test is declined in 3 versions:
- [Python Flask](./python-flask)
- [TypeScript Serverless](./typescript-serverless)
- [C# .NET](./c#-dotnet)

You can now start development by reading the README.md in the back-end test directory of the language of your choice.

**You must pick the one that is relevant to the position you're applying to.**

Good luck!
