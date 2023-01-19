FROM node:18-slim

# For using pg-native
RUN apt update -y && apt install -y python3 libpq-dev g++ make

# Remove user with UID 1000 as we may re-create it afterwards
RUN userdel "$(id -nu 1000)"

ARG USER_ID
ARG GROUP_ID

## Create default user:group for this container
RUN groupadd -g ${GROUP_ID} listingsapi;
RUN useradd -g listingsapi -u ${USER_ID} -ms /bin/bash listingsapi;

USER listingsapi

RUN mkdir /home/listingsapi/app
RUN chown listingsapi:listingsapi /home/listingsapi/app

WORKDIR /home/listingsapi/app

COPY --chown=listingsapi:listingsapi package*.json ./
RUN npm ci

COPY --chown=listingsapi:listingsapi . .
