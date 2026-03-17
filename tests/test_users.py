import allure
import pytest

from clients.user_client import UserClient


@allure.feature("Users")
class TestGetUsers:

    @allure.title("Получение списка пользователей - статус 200")
    @pytest.mark.parametrize("page_number", [1, 2])
    def test_get_users_status_200(self, user_client: UserClient, page_number: int):
        response = user_client.get_users(page=page_number)
        assert response.status_code == 200


    @allure.title("Получение списка пользователей - пустая страница")
    @pytest.mark.parametrize("page_number", [3, 4])
    def test_get_users_status_200(self, user_client: UserClient, page_number: int):
        response = user_client.get_users(page=page_number)
        response_json = response.json()
        data = response_json.get("data", None)
        assert response.status_code == 200
        assert len(data) == 0