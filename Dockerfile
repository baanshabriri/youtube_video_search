FROM python:3.9.16-alpine
ENV PYTHONNUNBUFFERED=1
WORKDIR /usr/src/app
COPY . ./
RUN pip install -r requirements.txt