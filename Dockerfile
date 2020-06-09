FROM python:3.7.6-slim-buster
# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
# Set work directory
WORKDIR /tmp
# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y libpq-dev gcc
# Install python dependencies
COPY Pipfile Pipfile.lock /tmp/
RUN pipenv install --system --deploy
RUN apt-get autoremove -y gcc
# Creates user so we do not run our image as root. (best practice)
#  Run this after you install dependencies to avoid permission errors on build.
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser
# Install application into container
COPY . .
