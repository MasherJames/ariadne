#pull base iamge
FROM node:12.10.0-alpine

#set woking directory
WORKDIR /gateway

#add /gateway/node_modules/.bin to $PATH
ENV PATH /gateway/node_modules/.bin:$PATH

#install and cache gateway dependencies
COPY package.json /gateway/package.json
RUN yarn

# Copy project
COPY . /gateway

ENV PORT 4000

EXPOSE 4000
#start gateway
CMD ["yarn", "start-gateway"]
