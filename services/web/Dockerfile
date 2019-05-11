FROM node as build
WORKDIR /app
COPY . .
RUN yarn install --silent
RUN yarn build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]