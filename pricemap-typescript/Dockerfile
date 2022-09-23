FROM node:16-slim

# Remove user with UID 1000 as we may re-create it afterwards
RUN userdel "$(id -nu 1000)"

ARG USER_ID
RUN useradd -ms /bin/bash pricemap
RUN if [ "$(id -u pricemap)" != "${USER_ID}" ]; then usermod -u ${USER_ID} pricemap ; fi

ARG GROUP_ID
# Create group if not found in /etc/group
RUN if ! $(awk -F':' '{print $3}' /etc/group |grep -q ${GROUP_ID}) ; then groupadd -g ${GROUP_ID} appgroup; fi
# append group for application user
RUN usermod -a -G ${GROUP_ID} pricemap

USER pricemap
WORKDIR /home/pricemap/app

COPY package*.json ./
RUN npm ci

COPY . .
