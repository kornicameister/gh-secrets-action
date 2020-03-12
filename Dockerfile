FROM python:3.8-alpine3.10 as base

RUN pip install --upgrade pip==20.0.1
COPY python/ghsa ./ghsa

FROM base AS build

RUN apk --update \
    add --no-cache --virtual build_dependencies \
        alpine-sdk=1.0-r0 \
        libc-dev=0.7.1-r0 \
        libressl-dev=2.7.5-r0 \
        libffi-dev=3.2.1-r6 \
        python3-dev=3.7.5-r1

WORKDIR /app

COPY python/requirements.txt ./requirements.txt
COPY python/ghsa ./ghsa

RUN pip install -r ./requirements.txt && rm -rf ./requirements.txt
RUN apk del build_dependencies && rm -rf /root/.cache

FROM build AS prod

RUN apk add --no-cache tini=0.18.0-r0

WORKDIR /app
ENV PYTHONPATH=/app

COPY --from=build /app/ghsa ./ghsa

ENTRYPOINT ["/sbin/tini", "--"]
CMD ["python", "-m", "ghsa"]
