FROM node:8.1.0-alpine
WORKDIR /app
COPY . .
RUN yarn install

EXPOSE 5000
CMD ["yarn", "watch:silent"]
