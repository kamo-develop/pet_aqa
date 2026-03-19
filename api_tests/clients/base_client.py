import requests
from requests import Response


class BaseClient:
    """
    Базовый HTTP-клиент
    """

    def __init__(self, base_url, x_api_key):
        self.base_url = base_url
        self.session = requests.session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "x-api-key": x_api_key
        })

    def get(self, endpoint: str, **kwargs) -> Response:
        return self.session.get(url=f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint: str, **kwargs) -> Response:
        return self.session.post(url=f"{self.base_url}{endpoint}", **kwargs)

    def put(self, endpoint: str, **kwargs) -> Response:
        return self.session.put(url=f"{self.base_url}{endpoint}", **kwargs)

    def patch(self, endpoint: str, **kwargs) -> Response:
        return self.session.patch(url=f"{self.base_url}{endpoint}", **kwargs)

    def delete(self, endpoint: str, **kwargs) -> Response:
        return self.session.delete(url=f"{self.base_url}{endpoint}", **kwargs)
