# pull official base image
FROM python:3.9.0-slim-buster

# set working directory
WORKDIR /usr/project/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean


# add and install requirements
COPY ./requirements-dev.txt .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements-dev.txt

# add app
COPY . .

# run server
COPY ./entrypoint.sh .
RUN chmod +x /usr/project/app/entrypoint.sh