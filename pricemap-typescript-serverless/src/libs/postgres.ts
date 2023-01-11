import postgres from "postgres";

console.log(process.env.PGHOST)

const sql = postgres({
  host: process.env.PGHOST,
  database: process.env.PGDATABASE,
  username: process.env.PGUSER,
  pass: process.env.PGPASSWORD,
});

export { sql };
