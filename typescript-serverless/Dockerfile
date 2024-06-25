FROM node:20-slim

# For using pg-native
RUN apt update -y && apt install -y python3 libpq-dev g++ make

# Remove user with UID 1000 as we may re-create it afterwards
RUN userdel "$(id -nu 1000)"

ARG USER_ID
ARG GROUP_ID

## Create default user:group for this container
RUN groupadd -g ${GROUP_ID} listingapi;
RUN useradd -g listingapi -u ${USER_ID} -ms /bin/bash listingapi;

USER listingapi

RUN mkdir /home/listingapi/app
RUN chown listingapi:listingapi /home/listingapi/app

WORKDIR /home/listingapi/app

COPY --chown=listingapi:listingapi package*.json ./
RUN npm ci

COPY --chown=listingapi:listingapi . .
