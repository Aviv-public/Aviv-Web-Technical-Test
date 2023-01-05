#!/usr/bin/env make

.DEFAULT_GOAL: help

MAKEFLAGS=--no-print-directory

DOCKER_COMPOSE?=docker-compose -p owner-technical-test

.PHONY: help
help: ## List all Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

##
## Containers 📦
## -------
##
.PHONY: build
build: ## Builds the docker image associated with the project
	docker-compose build --build-arg USER_ID=$(shell id -u $$USER) --build-arg GROUP_ID=$(shell id -g $$USER)

.PHONY: run
run: ## Start the containers
	$(DOCKER_COMPOSE) up -d

.PHONY: clean
clean: ## Remove containers
	$(DOCKER_COMPOSE) down --remove-orphans

.PHONY: clean-all
clean-all: ## Remove containers and volumes
	$(DOCKER_COMPOSE) down --remove-orphans -v

.PHONY: python-shell-pricemap-container
python-shell-pricemap-container: ## Run a bash on pricemap-python container
	$(DOCKER_COMPOSE) exec -T pricemap-python bash


##
## Import listing
## --------
##
.PHONY: python-import-listings
python-import-listings: ## Run a command to import listings into pricemap database
	$(DOCKER_COMPOSE) exec -T pricemap-python ./pricemap/console.py import-listings

##
## Tests
## --------
##
.PHONY: python-tests
python-tests: python-install-dev ## Execute tests
	$(DOCKER_COMPOSE) exec -T pricemap pipenv run pytest -vv --ff --exitfirst

##
## Code Analysis 🔎
## -----
##
.PHONY: code-analysis complexity format style
python-code-analysis: python-complexity python-format python-style ## Run the all code Analysis (code complexity, code format and code style)

.PHONY: complexity format style
python-complexity: ## Compute Cyclomatic complexity (McCabe) and maintainability check
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c \
		"radon cc -s -n B pricemap | tee /tmp/cc.txt && if [ -s /tmp/cc.txt ]; then exit 1; fi"

	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c \
		"radon mi -n B pricemap | tee /tmp/mi.txt && if [ -s /tmp/mi.txt ]; then exit 1; fi"

.PHONY: format style
python-format: ## Format code. e.g Prettier (js), format (golang)
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "isort pricemap tests; black ."

.PHONY: style
python-style: ## Check lint, code styling rules. e.g. pylint, phpcs, eslint, style (java) etc ...
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "mypy pricemap"
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "flake8 pricemap tests"
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "black --check ."
