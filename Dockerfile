# Use an official Python runtime as a base image
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && apt-get clean
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root

COPY . /app/
EXPOSE 8000
CMD ["sh", "-c", "poetry run python teams_py/manage.py migrate && poetry run python teams_py/manage.py runserver 0.0.0.0:8000"]
