build:
	docker-compose build

run:
	docker-compose up

clean:
	docker-compose down --remove-orphans

clean-all:
	docker-compose down --remove-orphans -v
