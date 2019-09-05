# pull base image
FROM python:3.7-alpine

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
WORKDIR /usr/src/employees_service

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/employees_service/Pipfile
RUN pipenv install --skip-lock --system --dev

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/employees_service/entrypoint.sh

# Copy project
COPY . /usr/src/employees_service
RUN ["chmod", "+x", "/usr/src/employees_service/entrypoint.sh"]
# Run entrypoint.sh
ENTRYPOINT ["/usr/src/employees_service/entrypoint.sh"]