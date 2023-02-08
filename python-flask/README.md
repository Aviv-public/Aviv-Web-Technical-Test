# Python Flask

Welcome to the Python Flask version of this test. This README lists the specificities of this application
and how to start developing on this codebase. For more general information about the test, refer to the [main README](../README.md).

## Getting started

### Existing codebase

This project uses the Flask framework to serve the ListingAPI endpoints and SQLAlchemy to persist entities.
Furthermore, we implemented it using `Hexagonal Architecture` (more details on this [article](https://alexgrover.me/posts/python-hexagonal-architecture)).

The project can be improved on different ways. You are totally free to improve the tests, codebase, etc. as you want.
You can explain your improvements and choices on the [SOLUTION.md](../SOLUTION.md) file 

### Develop

To start developing, a Makefile in folder `/python-flask/` will help you.

Here are some How-to guides to give you some common recipes.

## How-to guides

### Run local server

Run this command:

```shell
make run
```

It will start the API and the database in Docker containers.
The API will be serverd over the port `8080` in development mode with automatic reload when you edit your source code.
You can then start querying the API!

### Stop local server

Run this command:

```shell
make stop
```

It will stop the API and the database currently running.

### Force re-build of the API Docker container

Run this command:

```shell
make build
```

If you use JetBrains IDE, you can add a Local Docker code interpreter, based on a pulled image with tag `ghcr.io/meilleursagents/aviv-technical-test/python-flask:latest`.

### Clear all existing Docker images, volumes and containers

Run this command:

```shell
make clear
```


### Getting a shell in the Docker container 

If you want to go into the python container to execute custom commands, you can run the following command:

```shell
make shell
```

### Execute automatic tests

There are some existing tests in the project (both unit and integration).
To be sure that your modification keep working with the existing codebase, you can run:

```shell
make test
```

### Applying and checking code standards

One command is useful to automatically format your source code:

```shell
make format
```

But it doesn't do everything automatically, so you can verify code style and best practices with this command:

```shell
make style
```

And finally, you can check the cyclomatic complexity of your implementation with this command:

```shell
make complexity
```

### Add/remove some dependencies

We use [Pipenv](https://pipenv.pypa.io/en/latest/index.html) to manage dependencies.
It's based on the [Pipfile](/Pipfile) file.
It locks dependencies by automatically to the [Pipfile.lock](/Pipfile.lock) file.
You should never manually edit this last one!

After editing the Pipfile, you can lock dependencies and then re-build the Docker image by executing these two commands:
```shell
make lock-dependencies
make build
```

If you use JetBrains IDE, then you simply have to reload your interpreter by re-selecting it in the lower-right task bar.

### Visualize some listings

To help you during the implementation, we created a python script that will generate for you 10 `listings` payloads.
```shell
make generate-random-listings
```

**NB** : The script does not take care about price history for now. It's up to you to modify it if you need it :)


### I need something else...

You can see available commands in Makefile by running:
```shell
make help
```

Feel free to contact us by Slack! :)
