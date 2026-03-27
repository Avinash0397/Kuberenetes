FROM ubuntu:latest
LABEL maintainer="Hifza Khan"

# Update and install dependencies
RUN apt-get update && apt-get install -y nodejs npm curl \
    && [ -e /usr/bin/node ] || ln -s /usr/bin/nodejs /usr/bin/node \
    && npm install -g http-server

# Copy the HTML UI into the container
COPY usr/apps/hello-docker /usr/apps/hello-docker

# Set working directory
WORKDIR /usr/apps/hello-docker

# Start HTTP server
CMD ["http-server", "-p", "8080", "-s"]

