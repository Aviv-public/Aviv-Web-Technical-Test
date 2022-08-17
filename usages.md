# How to use this project

## Starting the project
Starts applications and database.

```sh
make run
```

`ctrl + C` to stop.

## Rebuilding the project
This should not be necessary as done automatically on first start, but can allow to force the rebuild of the apps.

```sh
make build
```

## Entering a container
To enter the shell of the app container and run manual commands.

```sh
docker-compose run pricemap bash
```

You can also do it on the `listingapi` and `db`, but it should not be necessary.

## Cleaning-up
Destroy application containers. Useful as `docker-compose` reuses already existing containers by default.

```sh
make clean
```

To also delete application volumes (and remove persisted data, such as database entries):
```sh
make clean-all
```
