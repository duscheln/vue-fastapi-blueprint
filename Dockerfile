FROM node:14-slim

ADD ./backend /usr/app/src/backend
ADD ./frontend usr/app/src/frontend

WORKDIR /usr/app/src/frontend

RUN npm install 
RUN npm run build
