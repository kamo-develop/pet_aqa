from clients.base_client import BaseClient


class UserClient(BaseClient):

    def get_users(self, page: int = 1):
        return self.get("/api/users", params={"page": page})