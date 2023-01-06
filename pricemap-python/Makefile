#!/usr/bin/env make

.DEFAULT_GOAL: help

MAKEFLAGS=--no-print-directory

DOCKER_COMPOSE?=docker-compose -p owner-technical-test

define HEADER

---------------------
      PYTHON 🐍
---------------------
NB : Please add prefix "python-" just before running any command of that Makefile 🙏
example : "python-help" to the "help" command

endef
export HEADER

.PHONY: help
help: ## List all Python Makefile targets
	@printf "$$HEADER\n"
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

##
## Python Containers 📦
## -------
##
.PHONY: build
build: ## Builds the python docker image
	docker build -t ghcr.io/meilleursagents/backend-technical-test/pricemap-python .

.PHONY: shell-pricemap-container
shell-pricemap-container: ## Run a bash on pricemap-python container
	$(DOCKER_COMPOSE) exec -T pricemap-python bash


##
## Python Import listing
## --------
##
.PHONY: import-listings
import-listings: ## Run a command to import listings into pricemap database
	$(DOCKER_COMPOSE) exec -T pricemap-python ./pricemap/console.py import-listings

##
## Python Tests
## --------
##
.PHONY: tests
tests: ## Execute tests
	$(DOCKER_COMPOSE) run --rm -T pricemap-python pipenv run pytest -vv --ff

##
## Python mCode Analysis 🔎
## -----
##
.PHONY: code-analysis complexity format style
code-analysis: complexity format style ## Run the all code Analysis (code complexity, code format and code style)

.PHONY: complexity format style
complexity: ## Compute Cyclomatic complexity and maintainability check
	$(DOCKER_COMPOSE) run --rm -T pricemap-python bash -c \
		"radon cc -s -n B pricemap | tee /tmp/cc.txt && if [ -s /tmp/cc.txt ]; then exit 1; fi"

	$(DOCKER_COMPOSE) run --rm -T pricemap-python bash -c \
		"radon mi -n B pricemap | tee /tmp/mi.txt && if [ -s /tmp/mi.txt ]; then exit 1; fi"

.PHONY: format style
format: ## Format code.
	$(DOCKER_COMPOSE) run --rm -T pricemap-python bash -c "isort pricemap tests; black ."

.PHONY: style
style: ## Check lint, code styling rules
	$(DOCKER_COMPOSE) run --rm -T pricemap-python bash -c "mypy pricemap"
	$(DOCKER_COMPOSE) run --rm -T pricemap-python bash -c "flake8 pricemap tests"
	$(DOCKER_COMPOSE) run --rm -T pricemap-python bash -c "black --check ."
