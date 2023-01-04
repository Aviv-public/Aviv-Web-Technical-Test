FROM python:3.8-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

## Create default user:group for this container
RUN groupadd pricemap;
RUN useradd -g pricemap -ms /bin/bash pricemap;

# add script to wait for db container to be ready
COPY docker/wait-for-postgres.sh /home/pricemap/wait-for-postgres.sh

USER pricemap
COPY . /home/pricemap/app
RUN chmod +x /home/pricemap/console.py

RUN pip3 install pipenv

WORKDIR /home/pricemap/app
ENV PATH /home/pricemap/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/pricemap/app
