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
