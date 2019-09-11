FROM python:3.7.4-alpine

RUN apk --update --upgrade add gcc \
    musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev \
    font-noto \
    gdk-pixbuf-dev postgresql-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]
