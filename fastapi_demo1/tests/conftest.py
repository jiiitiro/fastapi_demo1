from typing import AsyncGenerator, Generator
import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport

from fastapi_demo1.main import app
from fastapi_demo1.routers.post import post_table, comment_table


@pytest.fixture(scope="session")
def anyio_backend():
    return "asyncio"


@pytest.fixture()
def client() -> Generator:
    yield TestClient(app)


@pytest.fixture(autouse=True)
def db() -> AsyncGenerator:
    post_table.clear()
    comment_table.clear()
    yield


@pytest.fixture()
async def async_client(client) -> AsyncGenerator:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=client.base_url) as ac:
        yield ac
