FROM python:3.9.16-alpine
ENV PYTHONNUNBUFFERED=1
COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip3 install -r requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app

COPY . /app

WORKDIR /app