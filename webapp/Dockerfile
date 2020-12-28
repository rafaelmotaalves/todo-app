FROM node:15.5.0-alpine3.10

WORKDIR /app

COPY package.json .

COPY yarn.lock .

RUN yarn

COPY . .

CMD ["yarn", "dev"]