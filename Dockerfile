FROM python:3.12.2-slim

COPY pyproject.toml ./
COPY . ./project
WORKDIR /project

RUN pip install --upgrade pip \
    && pip install poetry

RUN poetry install --no-interaction --no-cache --no-ansi --without test

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8118"]