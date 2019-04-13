FROM node:8.1.0-alpine as build
WORKDIR /app
COPY . .
RUN yarn install --silent
RUN yarn build:silent

FROM nginx:alpine
COPY --from=build /app/public /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]