# vi: set ft=dockerfile
FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y --force-yes \
        python3 \
        python3-setuptools \
        python3-dev \
        python3-pip \
        build-essential

RUN pip3 install  \
    -U --ignore-installed \
    flake8

VOLUME /workdir
VOLUME /results
COPY flake8 flake8

WORKDIR /workdir
CMD flake8 --output-file=/results/results.txt --config=/workdir/flake8

