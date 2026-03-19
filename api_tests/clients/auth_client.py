from requests import Response

from api_tests.clients.base_client import BaseClient


class AuthClient(BaseClient):

    def register(self, email: str, password: str) -> Response:
        payload = {
            "email": email,
            "password": password
        }
        return self.post("/api/register", json=payload)

    def login(self, email: str, password: str) -> Response:
        payload = {
            "email": email,
            "password": password
        }
        return self.post("/api/login", json=payload)
