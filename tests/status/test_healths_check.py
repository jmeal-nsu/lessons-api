import pytest
from httpx import AsyncClient


class TestHealthCheck:
    @pytest.mark.asyncio
    async def test_healthcheck_returns_200(self, test_client: AsyncClient):
        response = await test_client.get("healthcheck")
        assert response.status_code == 200
