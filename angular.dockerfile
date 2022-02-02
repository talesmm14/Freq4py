FROM node:14-alpine

RUN mkdir -p /front-end

WORKDIR /front-end

COPY ./front-end/package*.json /front-end/

RUN npm install

COPY ./front-end /front-end/

EXPOSE 4200

CMD ["npm", "start"]