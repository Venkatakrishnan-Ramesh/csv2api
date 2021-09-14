FROM alpine:3.4
MAINTAINER Roshan "dev.vividgoat@gmail.com"
COPY . /app
WORKDIR /app
RUN set -xe \
    && apt-get update -y \
    && apt-get install - y python3-pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
