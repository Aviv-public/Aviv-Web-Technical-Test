.DEFAULT_GOAL := help

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
