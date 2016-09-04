FROM python:3.5-alpine

RUN apk --update add git

RUN pip install git+https://github.com/nnewman/stewie.git@master

WORKDIR /opt/stewie

USER nobody
EXPOSE 8043
