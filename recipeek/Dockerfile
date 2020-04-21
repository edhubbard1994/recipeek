FROM node:alpine as build

RUN mkdir /app

COPY package.json package-lock.json /app/ 
WORKDIR /app 

RUN npm i

COPY . /app 

RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx","-g","daemon off;"]