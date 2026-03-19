import allure
import pytest

from api_tests.schemas.auth_schemas import RegisterResponse, LoginResponse, AuthErrorResponse


@allure.feature("Регистрация")
class TestRegister:

    @allure.title("Успешная регистрация - статус 200 и токен в ответе")
    def test_register_success(self, auth_client):
        response = auth_client.register(
            email="eve.holt@reqres.in",
            password="pistol"
        )

        assert response.status_code == 200
        body = RegisterResponse.model_validate(response.json())
        assert body.token is not None


    @allure.title("Регистрация без пароля - статус 400 и сообщение об ошибке")
    def test_register_without_password_returns_400(self, auth_client):
        response = auth_client.register(email="sydney@fife", password=None)

        assert response.status_code == 400
        body = AuthErrorResponse.model_validate(response.json())
        assert body.error == "Missing password"


    @allure.title("Регистрация без логина - статус 400 и сообщение об ошибке")
    def test_register_without_email_returns_400(self, auth_client):
        response = auth_client.register(email=None, password="12345")

        assert response.status_code == 400
        body = AuthErrorResponse.model_validate(response.json())
        assert body.error == "Missing email or username"



@allure.feature("Аутентификация")
class TestLogin:

    @allure.title("Успешный логин - статус 200 и токен в ответе")
    def test_login_success(self, auth_client):
        response = auth_client.login(
            email="eve.holt@reqres.in",
            password="cityslicka"
        )

        assert response.status_code == 200
        body = LoginResponse.model_validate(response.json())
        assert body.token is not None

    @allure.title("Логин без пароля - статус 400 и сообщение об ошибке")
    def test_login_without_password_returns_400(self, auth_client):
        response = auth_client.login(email="eve.holt@reqres.in", password=None)

        assert response.status_code == 400
        body = AuthErrorResponse.model_validate(response.json())
        assert body.error == "Missing password"


    @allure.title("Логин без email - статус 400 и сообщение об ошибке")
    def test_login_without_email_returns_400(self, auth_client):
        response = auth_client.login(email="", password="123")

        assert response.status_code == 400
        body = AuthErrorResponse.model_validate(response.json())
        assert body.error == "Missing email or username"


    @allure.title("Логин несуществующего пользователя - статус 400 и сообщение об ошибке")
    def test_login_nonexistent_user(self, auth_client):
        response = auth_client.login(email="wrong@email.com", password="12345")

        assert response.status_code == 400
        body = AuthErrorResponse.model_validate(response.json())
        assert body.error == "user not found"