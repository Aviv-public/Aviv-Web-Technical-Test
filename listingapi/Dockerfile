FROM python:3.8-slim

RUN useradd -ms  /bin/bash listingapi
COPY listingapi /home/listingapi/listingapi
COPY create_api_dataset.py /home/listingapi/create_api_dataset.py

USER listingapi
WORKDIR /home/listingapi/app

RUN pip3 install pipenv
COPY Pipfile Pipfile.lock ./

ENV PATH /home/listingapi/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/listingapi/app
