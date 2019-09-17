# pull base image
FROM python:3.7.4-alpine

# set environment variables
# console output should not be buffered by docker
# python won't write to .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps


# set working dir
WORKDIR /usr/src/product_service

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/product_service/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/product_service/entrypoint.sh

# Copy project
COPY . /usr/src/product_service

# Run
CMD python manage.py collectstatic --no-input --clear;python manage.py migrate