FROM node:20.11.1-alpine3.19
RUN mkdir /app
WORKDIR /app
RUN npm install -g @angular/cli
COPY package.json package-lock.json ./
RUN npm ci
COPY . /app
EXPOSE 4200
CMD ["ng", "serve","--host", "0.0.0.0"]