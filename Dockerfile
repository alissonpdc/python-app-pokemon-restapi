FROM ubuntu:22.04

# fix timezone
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install python
RUN apt update && \
    apt upgrade -y && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update  && \
    apt install python3.12 -y && \
    python3.12 --version

RUN apt install curl -y && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12 


WORKDIR /app
COPY ./src/requirements.txt .
RUN pip3.12 install -r requirements.txt

COPY ./src/app .

EXPOSE 8000

CMD ["fastapi", "run"]