FROM python:3.8-slim

## Create default user:group for this container
RUN groupadd group_listingapi;
RUN useradd -ms /bin/bash listingapi
RUN usermod -a -G group_listingapi listingapi

USER listingapi
COPY --chown=listingapi:listingapi listingapi /home/listingapi/app
RUN chown -R listingapi:listingapi /home/listingapi/app

WORKDIR /home/listingapi/app

RUN pip3 install pipenv
COPY --chown=listingapi:listingapi Pipfile Pipfile.lock ./

ENV PATH /home/listingapi/.local/bin:${PATH}
RUN pipenv lock
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/listingapi/app
