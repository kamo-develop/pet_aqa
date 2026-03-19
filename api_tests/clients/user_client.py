from requests import Response

from api_tests.clients.base_client import BaseClient


class UserClient(BaseClient):

    def get_users(self, page: int = 1):
        return self.get("/api/users", params={"page": page})

    def get_user_by_id(self, user_id: int):
        return self.get(f"/api/users/{user_id}")

    def create_user(self, first_name: str, last_name: str) -> Response:
        return self.post("/api/users", json={"first_name": first_name, "last_name": last_name})

    def update_user(self, user_id: int, first_name: str, last_name: str) -> Response:
        return self.put(f"/api/users/{user_id}", json={"first_name": first_name, "last_name": last_name})

    def partial_update_user(self, user_id: int, **fields) -> Response:
        return self.patch(f"/api/users/{user_id}", json=fields)

    def delete_user(self, user_id: int) -> Response:
        return self.delete(f"/api/users/{user_id}")