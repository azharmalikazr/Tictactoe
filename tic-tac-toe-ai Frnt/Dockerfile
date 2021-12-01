FROM node:16

WORKDIR /app

COPY ./ /app

RUN npm -g install npm@8.1.4


RUN npm install -g @angular/cli

EXPOSE 6000

CMD ng serve --host 0.0.0.0 --port 6000






#FROM nginx:alpine
#COPY --from=node /usr/local/app /usr/share/nginx/html