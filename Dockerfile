# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /usr/src/buffetdjgo

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev zlib-dev libjpeg jpeg-dev 

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/buffetdjgo/entrypoint.sh"]
