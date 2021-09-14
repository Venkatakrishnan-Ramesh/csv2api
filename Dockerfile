FROM alpine:3.4
MAINTAINER Roshan "dev.vividgoat@gmail.com"
COPY . /app
WORKDIR /app
RUN apk --update add \
      build-base python-dev \
      ca-certificates python \
      ttf-droid \
      py-pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
