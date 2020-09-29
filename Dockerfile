FROM python:3.8-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

RUN useradd -ms  /bin/bash pikachu

# add script to wait for db container to be ready
COPY docker/wait-for-postgres.sh /home/pikachu/wait-for-postgres.sh

COPY pikachu /home/pikachu/pikachu
COPY settings.py /home/pikachu/settings.py

USER pikachu
WORKDIR /home/pikachu/pikachu

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock ./

ENV PATH /home/pikachu/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/pikachu/
