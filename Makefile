.DEFAULT_GOAL := help

DOCKER_COMPOSE?=docker-compose -p owner-technical-test

.PHONY: help
help: ## List all Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

##
## Containers 📦
## -------
##
.PHONY: build run
build: ## Builds the docker image associated with the project
	docker-compose build --build-arg USER_ID=$(shell id -u $$USER) --build-arg GROUP_ID=$(shell id -g $$USER)

run: build ## Locally run the application
	docker-compose up

##
## Miscellaneous 🪄
## -------------
##
.PHONY: clean clean-all
clean: ## Remove temporary files and docker images
	docker-compose down --remove-orphans

clean-all: ## Remove temporary files, volumes and images
	docker-compose down --remove-orphans --rmi all -v

##
## Code Analysis 🔎
## -----
##
.PHONY: code-analysis complexity format style
python-code-analysis: python-complexity python-format python-style ## Run the all code Analysis (code complexity, code format and code style)

python-complexity: ## Compute Cyclomatic complexity (McCabe) and maintainability check
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c \
		"radon cc -s -n B pricemap | tee /tmp/cc.txt && if [ -s /tmp/cc.txt ]; then exit 1; fi"

	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c \
		"radon mi -n B pricemap | tee /tmp/mi.txt && if [ -s /tmp/mi.txt ]; then exit 1; fi"

python-format: ## Format code. e.g Prettier (js), format (golang)
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "isort pricemap tests; black ."

python-style: ## Check lint, code styling rules. e.g. pylint, phpcs, eslint, style (java) etc ...
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "mypy pricemap"
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "flake8 pricemap tests"
	$(DOCKER_COMPOSE) exec -T pricemap-python bash -c "black --check ."
