FROM python:3.10

COPY pip.conf /etc

RUN apt-get update -y && apt-get upgrade -y
RUN pip3 install sense-t-daw-aa-supply-chain-api
RUN pip3 install aiomysql

CMD ["daw_aa", "-c", "/opt/config.yml", "start"]