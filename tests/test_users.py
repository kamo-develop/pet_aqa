import allure
import pytest

from clients.user_client import UserClient
from schemas.user_schemas import UserListResponse, UserSingleResponse, CreateUserResponse, UpdateUserResponse


@allure.feature("Получение пользователей")
class TestGetUsers:

    @allure.title("Получение списка пользователей - статус 200")
    @pytest.mark.parametrize("page_number", [1, 2])
    def test_get_users_status_200(self, user_client: UserClient, page_number: int):
        response = user_client.get_users(page=page_number)
        assert response.status_code == 200

    @allure.title("Получение списка пользователей - пустая страница")
    @pytest.mark.parametrize("page_number", [3, 4])
    def test_get_empty_users_page(self, user_client: UserClient, page_number: int):
        response = user_client.get_users(page=page_number)
        response_json = response.json()
        data = response_json.get("data", None)
        assert response.status_code == 200
        assert len(data) == 0

    @allure.title("Тело ответа списка пользователей соответствует схеме")
    def test_get_users_schema(self, user_client: UserClient):
        response = user_client.get_users()
        body = UserListResponse.model_validate(response.json())
        assert len(body.data) > 0

    @allure.title("Получение пользователя по id - статус 200")
    @pytest.mark.parametrize("user_id", [1, 2, 10])
    def test_get_single_user_status_200(self, user_client: UserClient, user_id: int):
        response = user_client.get_user_by_id(user_id=user_id)
        assert response.status_code == 200

    @allure.title("Тело ответа конкретного пользователя соответствует схеме")
    def test_get_single_user_schema(self, user_client):
        user_id = 1
        response = user_client.get_user_by_id(user_id=user_id)
        body = UserSingleResponse.model_validate(response.json())
        assert body.data.id == user_id

    @allure.title("Несуществующий пользователь - статус 404")
    @pytest.mark.parametrize("user_id", [-1, 0, 500, 'abcd'])
    def test_get_nonexistent_user_returns_404(self, user_client: UserClient, user_id: int):
        response = user_client.get_user_by_id(user_id=user_id)
        assert response.status_code == 404



@allure.feature("Создание пользователей")
class TestCreateUser:

    @allure.title("Тело ответа при создании пользователя соответствует схеме")
    def test_create_user_schema(self, user_client):
        response = user_client.create_user("John", "Edwards")
        CreateUserResponse.model_validate(response.json())
        assert response.status_code == 201

    @allure.title("Создание пользователя")
    @pytest.mark.parametrize("first_name, last_name", [
        ("John", "Weaver"),
        ("Tobias", "Edwards"),
        ("", "")
    ])
    def test_create_user_status_201(self, user_client, first_name, last_name):
        response = user_client.create_user(first_name, last_name)
        body = CreateUserResponse.model_validate(response.json())

        assert response.status_code == 201
        assert body.first_name == first_name
        assert body.last_name == last_name



@allure.feature("Редактирование пользователя")
class TestUpdateUser:

    @allure.title("Полное обновление пользователя (PUT) — статус 200")
    def test_update_user_put_status_200(self, user_client):
        response = user_client.update_user(user_id=2, first_name="John", last_name="Edwards")

        assert response.status_code == 200

    @allure.title("Частичное обновление пользователя (PATCH) — статус 200")
    def test_update_user_patch_status_200(self, user_client):
        response = user_client.partial_update_user(user_id=2, job="Senior QA")

        assert response.status_code == 200

    @allure.title("Тело ответа при редактировании пользователя соответствует схеме")
    def test_update_user_contains_updated_at(self, user_client):
        response = user_client.update_user(user_id=2, first_name="John", last_name="Edwards")

        body = UpdateUserResponse.model_validate(response.json())

        assert body.updatedAt is not None


@allure.feature("Удаление пользователя")
class TestDeleteUser:

    @allure.title("Удаление пользователя — статус 204")
    def test_delete_user_status_204(self, user_client):
        response = user_client.delete_user(user_id=2)

        assert response.status_code == 204

    @allure.title("Тело ответа при удалении пустое")
    def test_delete_user_empty_body(self, user_client):
        response = user_client.delete_user(user_id=2)

        assert response.text == ""
