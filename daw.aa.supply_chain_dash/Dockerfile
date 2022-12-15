FROM node:16-bullseye as builder

WORKDIR /app
COPY . /app
RUN yarn install && yarn build 

FROM node:16-bullseye

COPY --from=builder /app/build /app
RUN yarn global add serve

CMD ["serve", "-s", "/app"]