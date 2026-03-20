import time

import allure

from ui_tests.generators.gen_data import generate_person
from ui_tests.pages.webtable_page import WebTablePage


@allure.feature('Таблица пользователей')
class TestWebTable:
    BASE_URL = "https://demoqa.com/webtables"

    @allure.title('Проверка добавления нового пользователя в таблицу')
    def test_web_table_add_person(self, driver):
        new_person = generate_person()
        web_table_page = WebTablePage(driver, self.BASE_URL)
        web_table_page.open()
        web_table_page.fill_new_person_form(new_person)
        table_result = web_table_page.get_all_persons_in_table()
        assert [str(new_person)] in table_result

    @allure.title('Проверка поиска пользователей в таблице')
    def test_web_table_search_person(self, driver):
        new_person = generate_person()
        web_table_page = WebTablePage(driver, self.BASE_URL)
        web_table_page.open()
        web_table_page.fill_new_person_form(new_person)
        key_word = new_person.lastname
        web_table_page.search_some_person(key_word)
        table_result = web_table_page.get_all_persons_in_table()

        assert any(key_word in row[0] for row in table_result)

    @allure.title('Проверка редактирования пользователя в таблице')
    def test_web_table_update_person_info(self, driver):
        new_person = generate_person()
        web_table_page = WebTablePage(driver, self.BASE_URL)
        web_table_page.open()
        web_table_page.fill_new_person_form(new_person)
        key_word = new_person.lastname
        web_table_page.search_some_person(key_word)
        age = web_table_page.update_person_info()
        table_result = web_table_page.get_all_persons_in_table()

        assert any(str(age) in row[0] for row in table_result)


