# Base image for building the application
FROM node:18.10.0 as builder

WORKDIR /build/app

COPY package-lock.json package.json ./
RUN npm ci

COPY *.* ./
COPY src ./src

RUN npm run build
