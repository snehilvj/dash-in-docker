FROM python:3.8

RUN pip install poetry==1.1.13

WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry export -f requirements.txt --without-hashes --output requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
