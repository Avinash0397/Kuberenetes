# Use alpine base image
FROM alpine

# Maintainer info
LABEL maintainer="Hifza Khan"

# Install Node.js
RUN apk update && apk add nodejs

# Copy files to container
COPY . /app

# Set working directory
WORKDIR /app

# Run the script on container start
CMD ["node", "index.js"]

