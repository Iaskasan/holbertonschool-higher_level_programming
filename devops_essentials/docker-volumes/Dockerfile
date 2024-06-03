FROM alpine:latest
RUN apk add --no-cache curl
COPY config.txt /config.txt
RUN mkdir -p /data
VOLUME [ "/data" ]