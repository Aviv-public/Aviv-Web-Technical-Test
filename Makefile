#!/usr/bin/env make

.DEFAULT_GOAL: help

MAKEFLAGS=--no-print-directory

DOCKER_COMPOSE?=docker-compose -p owner-technical-test

help: ## List all Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

##
## Containers 📦
## -------
##
build: ## Builds the docker image associated with the project
	docker-compose build --build-arg USER_ID=$(shell id -u $$USER) --build-arg GROUP_ID=$(shell id -g $$USER)

run: ## Start the containers
	$(DOCKER_COMPOSE) up -d

clean: ## Remove containers
	$(DOCKER_COMPOSE) down --remove-orphans

clean-all: ## Remove containers and volumes
	$(DOCKER_COMPOSE) down --remove-orphans -v

python-pricemap-container: ## Run a bash on pricemap-python container
	$(DOCKER_COMPOSE) exec -T pricemap-python bash


##
## Import listing
## --------
##
python-import-listings: ## Run a command to import listings into pricemap database
	$(DOCKER_COMPOSE) exec -T pricemap-python ./pricemap/console.py import-listings

##
## Python Installer
## --------
##
python-install: ## Install pricemap module dependencies
	$(DOCKER_COMPOSE) exec -T pricemap pipenv install --clear

python-require: ## Require a new package for the pricemap container (Use DEP='your package name')
	$(DOCKER_COMPOSE) exec -T pricemap pipenv install --clear $(DEP)

python-install-dev: ## Install pricemap dev module dependencies
	$(DOCKER_COMPOSE) exec -T pricemap pipenv install --dev --clear

##
## Tests
## --------
##
python-tests: python-install-dev ## Execute tests
	$(DOCKER_COMPOSE) exec -T pricemap pipenv run pytest -vv --ff --exitfirst
