import PostgresClient from "serverless-postgres";

export const postgres = new PostgresClient({
  application_name: "listingapi-typescript",
  host: process.env.PGHOST,
  database: process.env.PGDATABASE,
  user: process.env.PGUSER,
  password: process.env.PGPASSWORD,
});

/**
 * Utility function to turn a dictionnary to a set of
 * rows, variables and values for selecting, inserting or updating
 * data in a table.
 */
export function extractVariables(value: object) {
  const columns = Object.entries(value).map((row) => row[0]);
  const variables = Object.entries(value).map((_, index) => `$${index + 1}`);
  const values = Object.entries(value).map((row) => row[1]);

  return { columns, variables, values };
}
