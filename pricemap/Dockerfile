FROM python:3.8-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

RUN useradd -ms  /bin/bash pricemap

# add script to wait for db container to be ready
COPY docker/wait-for-postgres.sh /home/pricemap/wait-for-postgres.sh

COPY pricemap /home/pricemap/pricemap
COPY settings.py /home/pricemap/settings.py

USER pricemap
WORKDIR /home/pricemap/pricemap

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock ./

ENV PATH /home/pricemap/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/pricemap/
