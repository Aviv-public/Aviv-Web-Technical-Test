FROM node:16-slim

# Remove user with UID 1000 as we may re-create it afterwards
RUN userdel "$(id -nu 1000)"

## Create default user:group for this container
RUN groupadd pricemap;
RUN useradd -g pricemap -ms /bin/bash pricemap;

USER pricemap

# Force creation of directory by user to avoid permission issue
RUN mkdir /home/pricemap/app
RUN chmod 777 /home/pricemap/app
WORKDIR /home/pricemap/app

COPY package*.json ./
RUN npm ci

COPY . .
