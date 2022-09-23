import express from "express";
import path from "path";
import { updateData } from "./app";
import { geoms, getPrice } from "./api";

process.on("unhandledRejection", (e) => {
  throw e;
});

const app = express();
app.use(express.static(path.join(__dirname, "../static")));

app.get("/update_data", updateData);
app.get("/api/geoms", geoms);
app.get("/api/get_price/:cog", getPrice);

const port = 5000;
app.listen(port, async () => {
  console.log(`App listening on port ${port}`);
});
