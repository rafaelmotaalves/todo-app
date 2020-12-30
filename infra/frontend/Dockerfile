
# build environment
FROM node:15.5.0-alpine3.10 AS build

WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json

RUN yarn

COPY . /app

RUN yarn build

# production environment
FROM nginx:1.16.0-alpine

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]