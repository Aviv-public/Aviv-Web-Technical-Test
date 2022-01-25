FROM python:3.8-slim

# Install postgres client for waiting db container
RUN apt-get update && apt-get install --assume-yes postgresql-client

RUN useradd -ms /bin/bash pricemap
ARG USER_ID
RUN if [ "$(id -u pricemap)" != "${USER_ID}" ]; then usermod -u ${USER_ID} pricemap ; fi

ARG GROUP_ID
# Create group if not found in /etc/group
RUN if ! $(awk -F':' '{print $3}' /etc/group |grep -q ${GROUP_ID}) ; then groupadd -g ${GROUP_ID} appgroup; fi
# append group for application user
RUN usermod -a -G ${GROUP_ID} pricemap

# add script to wait for db container to be ready
COPY docker/wait-for-postgres.sh /home/pricemap/wait-for-postgres.sh

USER pricemap
COPY . /home/pricemap/app

RUN pip3 install pipenv

WORKDIR /home/pricemap/app
ENV PATH /home/pricemap/.local/bin:${PATH}
RUN pipenv install --deploy --system

ENV PYTHONPATH /home/pricemap/app
