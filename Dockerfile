FROM python:3.11-slim

WORKDIR /hotels_admin

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY poetry.lock pyproject.toml ./

RUN python -m pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false

COPY . /hotels_admin

LABEL project='hotels_admin' version=1.0

RUN poetry install --no-interaction --no-ansi --no-root