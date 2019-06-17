FROM ubuntu:latest

RUN apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y python python-dev python-pip python-virtualenv && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    pip install pyspark --no-cache-dir
  
WORKDIR /data

COPY *.py /data/
COPY build.sh /data/
COPY log4j.properties /data/
COPY spark.conf /data/
RUN chmod 0777 /data/*.sh
RUN chmod 0777 /data/*.py
ENTRYPOINT  ["./build.sh"]