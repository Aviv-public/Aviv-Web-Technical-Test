# Python Flask

Welcome to the Python Flask version of this test. This README lists the specificities of this application
and how to start developing on this codebase. For more general information about the test, refer to the [main README](../README.md).

## Getting started

To start developing, use the following command:

```shell
# Build the latest version of the Python image
make build

# Run Python project
make run
```

It will start the project and serve the API over the port `8080`. You can then start querying the API.

If you want to go into the python container to install dependencies or else, you can run the following command:

```shell
# Run a shell on the python-flask container
make shell
```

Finally, if you need more detail about available commands, you can run:
```shell
# Display all available commands
make help
```

## Testing

We added some unit and functional tests on the project.
To be sure that your modification keep working with the existing codebase, you can run:

```shell
# Run the tests of the project
make test
```

To follow coding best practices and standards, we added as well some useful commands that will check your implementation:

```shell
# Check the cyclomatic complexity of your implementation
make complexity

# Check the code style and best practices
make style
```

## Development

This project uses the Flask framework to serve the ListingsAPI endpoints and SQLAlchemy to persist entities.
Furthermore, we implemented it using `Hexagonal Architecture` (more details on this [article](https://alexgrover.me/posts/python-hexagonal-architecture)).

The project can be improved on different ways. You are totally free to improve the tests, codebase, etc... as you want.
You can explain your improvements and choices on the [SOLUTION.md](../SOLUTION.md) file 

### Payload generation

To help you during the implementation, we created a python script that will generate for you 10 `listings` payloads
```shell
# Run a shell on the python-flask container
make shell

python factory.py
```

**NB** : The script does not take care about price history for now. It's up to you to modify it if you need it :)
