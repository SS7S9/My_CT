FROM python:3.10

WORKDIR /app
COPY . /app

RUN apt-get update -y && apt-get upgrade -y
RUN pip3 install .
RUN pip3 install aiomysql

CMD ["daw_aa_api", "-c", "/opt/config.yml", "start"]