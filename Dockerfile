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

RUN chmod 0777 /data/*

ENTRYPOINT  ["./build.sh"]