from httpx import AsyncClient

import pytest
import pytest_asyncio

try:
    from src.main import app
except (NameError, ImportError):
    raise AssertionError(
        "Не обнаружен объект приложения `app`. Проверьте и поправьте: он должен быть доступен в модуле `src.main`.",
    )

pytest_plugins = ["tests.status.fixtures.base_requests", "pytest_asyncio"]


@pytest_asyncio.fixture()
async def test_client():
    # app.dependency_overrides[#dependency_name] = #fixture_fake_dependency
    async with AsyncClient(app=app, base_url="http://0.0.0.0:8118") as client:
        yield client
