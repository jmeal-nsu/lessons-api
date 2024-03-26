FROM python:3.12.2-slim

COPY . .

RUN pip install --upgrade pip \
    && pip install poetry

RUN poetry install --no-interaction --no-cache --no-ansi --without test

CMD ["./entrypoint.sh"]