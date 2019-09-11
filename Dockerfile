FROM python:3.7-alpine

RUN apk add --no-cache  --virtual .build-deps \
    postgresql-dev \
    gcc musl-dev jpeg-dev zlib-dev libffi-dev \
    cairo-dev pango-dev gdk-pixbuf-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["/app/entrypoint.sh"]
