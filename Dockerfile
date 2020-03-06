FROM python:3.8-alpine3.10 as build

RUN pip install --upgrade pip==20.0.1

FROM python:3.8-alpine3.10 as prod

COPY entrypoint.sh ./entrypoint.sh
RUN apk add --no-cache tini=0.18.0-r0

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["./entrypoint.sh"]
