import express, { Request, Response } from "express"

process.on("unhandledRejection", e => {
    throw e
})

const app = express()
app.get("/", (req: Request, res: Response) => {
    res.json({ hello: "world" })
})

const port = 5000
app.listen(port, () => {
    console.log(`App listening on port ${port}`)
})
