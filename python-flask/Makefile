#!/usr/bin/env make

.DEFAULT_GOAL: help

MAKEFLAGS=--no-print-directory

DOCKER_COMPOSE?=docker-compose -p aviv-technical-test

.PHONY: help
help: ## List all Python Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

##
## Python Containers 📦
## -------
##
.PHONY: build
build: ## Build the python docker image
	docker build --label python-flask --label aviv-technical-test -t ghcr.io/meilleursagents/backend-technical-test/pricemap-python .

.PHONY:
run:  ## Run a python-flask container
	$(DOCKER_COMPOSE) run -p 8080:8080 --rm python-flask python app.py

.PHONY: shell
shell: ## Open a bash shell on a python-flask container
	$(DOCKER_COMPOSE) run --rm python-flask bash

##
## Python Tests
## --------
##
.PHONY: test
test: ## Shortcut to launch all the test tasks (unit, functional and integration).
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
"COVERAGE_FILE=/tmp/.coverage pytest -p no:cacheprovider -Werror --cov . --cov-report term-missing -vv tests"

##
## Python Code Analysis 🔎
## -----
##
.PHONY: complexity
complexity: ## Compute cyclomatic complexity and maintainability check
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
		"radon cc -s -n B listingapi | tee /tmp/cc.txt && if [ -s /tmp/cc.txt ]; then exit 1; fi"

	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c \
		"radon mi -n B listingapi | tee /tmp/mi.txt && if [ -s /tmp/mi.txt ]; then exit 1; fi"

.PHONY: format
format: ## Format code
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c "isort tests listingapi && black ."


.PHONY: style
style: ## Check lint, code styling rules
	$(DOCKER_COMPOSE) run --user listingapi:listingapi --rm -T --no-deps python-flask bash -c "mypy tests listingapi && flake8 tests listingapi && isort tests listingapi -c && black --check ."

.PHONY: all
all: build format style test ## Build, format, check style and test
