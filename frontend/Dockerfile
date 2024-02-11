FROM node:20 AS angular-builder

WORKDIR /readings/frontend

COPY . .

RUN npm install -g @angular/cli

RUN npm install

EXPOSE 8080

CMD ["sh", "-c", "exec ng serve --host=0.0.0.0 --port=8080"]
