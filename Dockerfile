# Pull base image
FROM python:3.10.4-slim-bullseye

# Set enviriment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

#Install depencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y gettext libgettextpo-dev

# Copy project
COPY . .