FROM python:3.11-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

## Create default user:group for this container
RUN groupadd listingapi;
RUN useradd -g listingapi -ms /bin/bash listingapi;

# add script to wait for db container to be ready
COPY docker/wait-for-postgres.sh /home/listingapi/wait-for-postgres.sh

USER listingapi

RUN pip3 install pipenv

WORKDIR /home/listingapi/app
ENV PATH /home/listingapi/.local/bin:${PATH}

COPY --chown=listingapi:listingapi Pipfile /home/listingapi/Pipfile
COPY --chown=listingapi:listingapi Pipfile.lock /home/listingapi/Pipfile.lock

RUN pipenv install --deploy --system --dev

ENV PYTHONPATH /home/listingapi/app/

COPY --chown=listingapi:listingapi . /home/listingapi/app
