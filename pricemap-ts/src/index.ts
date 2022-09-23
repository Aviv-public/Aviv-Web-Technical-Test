import express, { Request, Response } from "express"
import { sql } from "./postgres"

process.on("unhandledRejection", e => {
    throw e
})

const app = express()
app.get("/", (req: Request, res: Response) => {
    res.json({ hello: "world" })
})

const port = 5000
app.listen(port, async () => {
    const test = await sql`
        SELECT * FROM geoplace
    `

    console.log(test)

    console.log(`App listening on port ${port}`)
})
