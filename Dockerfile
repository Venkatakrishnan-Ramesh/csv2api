FROM alpine:3.4

RUN apk --update add \
      build-base python-dev \
      ca-certificates python \
      ttf-droid \
      py-pip \
      py-jinja2 \
      py-twisted \
      py-dateutil \
      py-tz \
      py-requests \
      py-pillow \
      py-rrd && \
    apk del build-base python-dev && \
    rm -rf /var/cache/apk/* && \
    adduser -D -u 1001 noroot

USER noroot

CMD ["/bin/sh"]
