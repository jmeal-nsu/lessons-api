# lessons-api
API for lessons schedule project using Python and FastAPI

## Setup
*Install python 3.12+ compatiable with your OS: https://www.python.org/downloads/release/python-3121/*

Install poetry (Linux/MacOS)
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Install poetry (Windows)
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Install dependencies
```bash
poetry install
```

## Launch app on Localhost
```bash
poetry run uvicorn src.main:app --port 8118 --host 0.0.0.0 --reload
```

## Build with docker
```bash
docker build -t "tjest/lessons_api:$(poetry version -s)" .
```

# Development guides
## Alembic guide

При добавлении в базу новых сущностей или изменения уже существующих нужно сделать 3 шага:
### Добавить/Поменять определения в коде.
Было:
```python
class User(PostgresBase):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    roles = Column(
        ARRAY(String), nullable=False, default=list()
    )
```
Стало:
```python
# src/schemas/users.py
class Role(Enum):
    ADMIN = "admin"

class User(PostgresBase):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)
    roles: list[str] = Column(ARRAY(PgEnum(Role, create_type=True)), nullable=False, default=list())

# src/schemas/log_entry.py
class LogEntry(PostgresBase):
    __tablename__ = "logs"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    note: Mapped[str] = mapped_column()
```
То есть меняем код прямо в сурсах.
### Автосгенерировать миграцию.
```bash
poetry run alembic revision --autogenerate -m "change Role to Enum and create LogEntry table"
```
Файлик со сгенерированной миграцией автоматически добавится в `alembic/versions/`.
### Запушить изменения в миграциях с кодом
```bash
git add -A
git commit -am "LogEntry created, enum Role created, migrations file created"
git push origin mybranch
```
При мердже в мейн будет вызван `deploy`, который запушит контейнер да dockerhub и развернёт контейнер на сервере.
При старте контейнера будет вызвано `poetry run alembic upgrade head`, что и приведёт к миграции в базе.