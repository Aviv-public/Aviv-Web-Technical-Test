build:
	docker-compose build --build-arg USER_ID=$(shell id -u $$USER) --build-arg GROUP_ID=$(shell id -g $$USER)

run:
	docker-compose up

clean:
	docker-compose down --remove-orphans

clean-all:
	docker-compose down --remove-orphans -v
