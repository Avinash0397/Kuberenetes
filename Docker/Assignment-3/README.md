# Assignment 3: Node.js Hostname Docker Example

This assignment demonstrates how to build and run a lightweight Docker container using Alpine Linux and Node.js, which prints the container's hostname.

---

## 1. Project Structure

```
.
├── Dockerfile
├── index.js
└── README.md
```

---

## 2. index.js

Create a file named `index.js` with the following content:

```js
var os = require("os");
var hostname = os.hostname();
console.log("hello from " + hostname);
```

---

## 3. Dockerfile

Create a file named `Dockerfile` with the following content:

```dockerfile
FROM alpine

LABEL maintainer="Your Name <your.email@example.com>"

RUN apk update && apk add nodejs

COPY . /app

WORKDIR /app

CMD ["node", "index.js"]
```

Replace `"Your Name <your.email@example.com>"` with your actual name and email.

---

## 4. Build the Docker Image

Build the Docker image and tag it as `hello:v0.1`:

```bash
docker build -t hello:v0.1 .
```
![image](https://github.com/user-attachments/assets/cd798c2a-67cd-4e06-b007-4c4c41a2265e)

---

## 5. Run the Docker Container

Run the container:

```bash
docker run --rm hello:v0.1
```


You should see output similar to:

```
hello from <container-hostname>
```
![image](https://github.com/user-attachments/assets/068fd5d4-b2ec-4c61-8757-f14608a66307)

---

## 6. Clean Up

If you want to remove the image:

```bash
docker rmi hello:v0.1
```

---

## Notes

- This example uses the minimal Alpine Linux base image for a small and fast container.
- The script prints the hostname of the running container.
- Make sure both `Dockerfile` and `index.js` are in the same directory when building the image.

---
