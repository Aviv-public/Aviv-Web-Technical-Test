# Base image for building the application
FROM node:18.10.0 as builder

WORKDIR /build/app

RUN npm install -g pnpm && \
    npm remove -g npm

COPY pnpm-lock.yaml package.json ./
RUN pnpm install

COPY *.* ./
COPY src ./src
RUN pnpm run lint:check
RUN pnpm run build

# Base image for testing the application
FROM builder as tester
RUN pnpm run test