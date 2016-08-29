FROM python:3.5-alpine

RUN mkdir -p /opt/stewie
ADD . /opt/stewie

RUN cd /opt/stewie && python3 setup.py install

WORKDIR /opt/stewie/stewie

USER nobody
EXPOSE 5001 8043
