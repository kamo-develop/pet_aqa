import os

import pytest
from dotenv import load_dotenv

from api_tests.clients.auth_client import AuthClient
from api_tests.clients.user_client import UserClient

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL")
    assert url, "BASE_URL не задан в .env файле"
    return url


@pytest.fixture(scope="session")
def x_api_key():
    key = os.getenv("X-API-KEY")
    assert key, "X-API-KEY не задан в .env файле"
    return key


@pytest.fixture(scope="session")
def user_client(base_url, x_api_key) -> UserClient:
    return UserClient(base_url, x_api_key)

@pytest.fixture(scope="session")
def auth_client(base_url, x_api_key) -> AuthClient:
    return AuthClient(base_url, x_api_key)
