FROM node:alpine

RUN mkdir /app

COPY package.json package-lock.json /app/ 
WORKDIR /app 

RUN npm i

COPY . /app 
EXPOSE 3000

ENTRYPOINT ["npm"]
CMD ["start"]