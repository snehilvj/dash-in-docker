FROM python:3.8

ENV REDIS_PORT=6379
ENV DASH_PORT=8050

ARG POETRY_VERSION
RUN pip install poetry==${POETRY_VERSION}

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export -f requirements.txt --without-hashes --output requirements.txt
RUN pip install -r requirements.txt

COPY . .
ARG DASH_PORT
CMD gunicorn -b 0.0.0.0:${DASH_PORT} --reload app:server
