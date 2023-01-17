FROM python:3.11-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

## Create default user:group for this container
RUN groupadd pricemap;
RUN useradd -g pricemap -ms /bin/bash pricemap;

# add script to wait for db container to be ready
COPY docker/wait-for-postgres.sh /home/pricemap/wait-for-postgres.sh

USER pricemap

RUN pip3 install pipenv

WORKDIR /home/pricemap/app
ENV PATH /home/pricemap/.local/bin:${PATH}

COPY --chown=pricemap:pricemap Pipfile /home/pricemap/Pipfile
COPY --chown=pricemap:pricemap Pipfile.lock /home/pricemap/Pipfile.lock

RUN pipenv install --deploy --system --dev

ENV PYTHONPATH /home/pricemap/app/

COPY --chown=pricemap:pricemap . /home/pricemap/app
