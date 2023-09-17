# AVIV technical test solution

## Notes

I spent about 2 hours 30 minutes to complete the test.

The implementation of the price history feature was done in a way that is consistent with the existing codebase. The same structure and naming conventions were used to ensure that the code is easy to understand and maintain.

A new table was created in the PostgreSQL database to store the price history of each listing. This was done to keep the price history separate from the listing data and to allow for efficient retrieval of the price history.

A new repository file `prices.ts` was created. This file contains the logic for adding a new price entry to the db and retrieving the price history of a specific listing from the db.

The **updateListing** and **addListing** functions were updated to add a new entry in the price table whenever a listing is updated or added.

The **getListingPrices** function was updated to retrieve the price history of a specific listing from the database.

Unit tests were written for the price repository to ensure that the new functionality works as expected.

## Questions

- **What is missing with your implementation to go to production?**

  While the core functionality is implemented, there are a few areas that could be improved before going to production:

  - More comprehensive error handling and logging for better troubleshooting and monitoring. (Using something like Sentry and CloudWatch)
  - Additional tests for the listings repository and integration tests for both listings and prices using a test db.
  - Sorting of prices based on the preference of the frontend.
  - Pagination for both listings and price history.
  - Require authentication when adding or updating a listing.

- **How would you deploy your implementation?**

  The implementation can be deployed using a continuous integration/continuous deployment (CI/CD) pipeline. The pipeline would include stages for building the application, running tests, and deploying the application to a production environment.

- **If you had to implement the same application from scratch, what would you do differently?**

  If starting from scratch, I might consider:

  - Using a NoSQL database like MongoDB if our data doesn't require a relational database. This could potentially improve performance and scalability.
  - Using an ORM library to simplify the database operations.

- **The application aims at storing hundreds of thousands listings and millions of prices, and be accessed by millions of users every month. What should be anticipated and done to handle it?**

  To handle this scale, the application should be designed to be highly scalable and performant. This could involve:

  - Using a distributed database system like Amazon DynamoDB.
  - Using load balancing to distribute traffic.
  - Implementing caching with Redis to reduce database load.
  - Monitor and optimize the application code for performance.
  - Using AWS Auto Scaling to automatically adjust the number of server instances based on the load.
