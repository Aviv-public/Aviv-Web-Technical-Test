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
	docker build --label python-flask --label owner-technical-test -t ghcr.io/meilleursagents/backend-technical-test/pricemap-python .

.PHONY: shell-listingapi-container
shell-listingapi-container: ## Run a bash on python-flask container
	$(DOCKER_COMPOSE) exec python-flask bash

##
## Python Tests
## --------
##
.PHONY: tests
tests: ## Execute tests
	$(DOCKER_COMPOSE) run --rm -T python-flask pipenv run pytest -vv --ff

##
## Python Code Analysis 🔎
## -----
##
check-code-analysis: complexity format-check style ## Run the all code Analysis (code complexity, code format and code style) without changing code
code-analysis: complexity format-code style ## Run the all code Analysis (code complexity, code format and code style)

.PHONY: complexity
complexity: ## Compute Cyclomatic complexity and maintainability check
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
		"radon cc -s -n B listingapi | tee /tmp/cc.txt && if [ -s /tmp/cc.txt ]; then exit 1; fi"

	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
		"radon mi -n B listingapi | tee /tmp/mi.txt && if [ -s /tmp/mi.txt ]; then exit 1; fi"

.PHONY: format-code
format-code: ## Format code
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c "isort tests listingapi && black ."

.PHONY: format-check
format-check: ## Check code format
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c "isort tests listingapi -c && black --check ."

.PHONY: style
style: ## Check lint, code styling rules
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c "mypy tests listingapi && flake8 tests listingapi"


##
## Test 🧪
## -----
##
.PHONY: test
test: ## Shortcut to launch all the test tasks (unit, functional and integration).
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
"COVERAGE_FILE=/tmp/.coverage pytest -p no:cacheprovider -Werror --cov . --cov-report term-missing -vv tests"

.PHONY: test-dev
test-dev:  ## Shortcut to launch all the test tasks (unit, functional and integration).
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
"pytest -Werror -vv tests"
