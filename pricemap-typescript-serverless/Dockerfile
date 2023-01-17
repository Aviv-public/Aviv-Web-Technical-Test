FROM node:16-slim

# For using pg-native
RUN apt update -y && apt install -y python3 libpq-dev g++ make

# Remove user with UID 1000 as we may re-create it afterwards
RUN userdel "$(id -nu 1000)"

## Create default user:group for this container
RUN groupadd pricemap;
RUN useradd -g pricemap -ms /bin/bash pricemap;

RUN mkdir /home/pricemap/app
WORKDIR /home/pricemap/app

COPY package*.json ./
RUN npm ci
VOLUME /home/pricemap/app/node_modules

COPY . .

RUN chown -R pricemap:pricemap /home/pricemap/app
USER pricemap
