FROM python:3.7.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache --virtual build-deps gcc python3-dev \ 
    musl-dev postgresql-dev jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev \ 
    tiff-dev tk-dev tcl-dev libffi-dev py-cffi libxml2-dev libxslt-dev \ 
    postgresql-client libc-dev build-base libxml2 libxslt libjpeg-turbo-dev \ 
    libpng-dev openblas-dev libressl-dev bash git

RUN addgroup -S xuzer && adduser -S -G xuzer xuzer

RUN pip install --upgrade pip
RUN pip install --no-cache-dir numpy==1.16.0 pandas==1.0.3

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir celery[redis] amqp redis celery==4.4.2
RUN pip install --no-cache-dir Flask-Migrate
RUN pip install --no-cache-dir Flask-Script
RUN pip install --no-cache-dir flask-marshmallow==0.11.0 marshmallow \
        marshmallow-sqlalchemy
RUN pip install --no-cache-dir sqlalchemy-migrate==0.7.2 
RUN pip install --no-cache-dir Flask-Login==0.5.0
RUN mkdir -p /main

WORKDIR /main

COPY ./dockerfiles/web/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./dockerfiles/web/runserver.sh /runserver.sh
RUN chmod +x /runserver.sh

ENTRYPOINT ["/entrypoint.sh"]