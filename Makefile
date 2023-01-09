#!/usr/bin/env make

.DEFAULT_GOAL: help

DOCKER_COMPOSE?=docker-compose -p owner-technical-test

define PYTHON_HEADER

---------------------
      PYTHON 🐍
---------------------
NB : Please add prefix "python-" just before running any command of that Makefile 🙏
example : "python-help" to the "help" command

endef
export PYTHON_HEADER

.PHONY: help
help: ## List all Makefile targets
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
	@printf "$$PYTHON_HEADER\n"
	@$(MAKE) python-help

##
## Containers 📦
## -------
##
.PHONY: build
build: ## Builds the docker image associated with the project
	$(MAKE) python-build

.PHONY: run
run: ## Start the containers
	$(DOCKER_COMPOSE) up -d

.PHONY: clean
clean: ## Remove containers
	$(DOCKER_COMPOSE) down --remove-orphans

.PHONY: clean-all
clean-all: ## Remove containers and volumes
	$(DOCKER_COMPOSE) down --remove-orphans -v
	docker image prune --filter label=owner-technical-test -af

# Extract the string right after `python-` and propagate it to Python sub Makefile
# Example :
# 	- "python-help" will run "help" from the python-pricemap Makefile
# 	- "python-import-all-listings" will run "import-all-listings" from the python-pricemap Makefile
python-%: ## Execute Python command that come from the Python sub Makefile
	@$(MAKE) -C pricemap-python $${$@}
