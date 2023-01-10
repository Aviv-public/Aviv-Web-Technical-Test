#!/usr/bin/env make

.DEFAULT_GOAL: help

MAKEFLAGS=--no-print-directory

DOCKER_COMPOSE?=docker-compose -p owner-technical-test

.PHONY: help
help: ## List all Python Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

##
## Python Containers 📦
## -------
##
.PHONY: build
build: ## Builds the python docker image
	docker build --label pricemap-python --label owner-technical-test -t ghcr.io/meilleursagents/backend-technical-test/pricemap-python .

.PHONY: shell-pricemap-container
shell-pricemap-container: ## Run a bash on pricemap-python container
	$(DOCKER_COMPOSE) exec -T pricemap-python bash


##
## Python Import listing
## --------
##
.PHONY: import-listings
import-all-listings: ## Run a command to import listings into pricemap database
	$(DOCKER_COMPOSE) exec -T pricemap-python ./pricemap/controllers/cli/console.py import-all-listings

##
## Python Tests
## --------
##
.PHONY: tests
tests: ## Execute tests
	$(DOCKER_COMPOSE) run --rm -T pricemap-python pipenv run pytest -vv --ff

##
## Python Code Analysis 🔎
## -----
##
check-code-analysis: complexity format-check style ## Run the all code Analysis (code complexity, code format and code style) without changing code
code-analysis: complexity format-code style ## Run the all code Analysis (code complexity, code format and code style)

.PHONY: complexity
complexity: ## Compute Cyclomatic complexity and maintainability check
	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps pricemap-python bash -c \
		"radon cc -s -n B pricemap | tee /tmp/cc.txt && if [ -s /tmp/cc.txt ]; then exit 1; fi"

	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps pricemap-python bash -c \
		"radon mi -n B pricemap | tee /tmp/mi.txt && if [ -s /tmp/mi.txt ]; then exit 1; fi"

.PHONY: format-code
format-code: ## Format code
	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps pricemap-python bash -c "isort tests pricemap && black ."

.PHONY: format-check
format-check: ## Check code format
	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps pricemap-python bash -c "isort tests pricemap -c && black --check ."

.PHONY: style
style: ## Check lint, code styling rules
	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps pricemap-python bash -c "mypy tests pricemap && flake8 tests pricemap"


##
## Test 🧪
## -----
##
.PHONY: test
test: ## Shortcut to launch all the test tasks (unit, functional and integration).
	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps --no-deps pricemap-python bash -c \
"pytest -Werror --cov . --cov-report term-missing --cov-report xml --junitxml=junit-coverage.xml --cov-config .coveragerc -vv tests"

.PHONY: test-dev
test-dev:  ## Shortcut to launch all the test tasks (unit, functional and integration).
	$(DOCKER_COMPOSE) run --user pricemap:pricemap --rm -T --no-deps --no-deps pricemap-python bash -c \
"pytest -Werror -vv tests"
