FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y sudo \
    && mkdir -p /Data/Ninjas/Mohan /Data/Ninjas/Uma /Data/Ninjas/Shikha /Data/Ninjas/Mayank \
    && useradd -m Mohan \
    && chown Mohan:Mohan /Data/Ninjas/Mohan \
    && chmod 700 /Data/Ninjas/Mohan \
    && chmod 755 /Data/Ninjas/Uma /Data/Ninjas/Shikha /Data/Ninjas/Mayank

USER Mohan

WORKDIR /home/Mohan

CMD ["/bin/bash"]

