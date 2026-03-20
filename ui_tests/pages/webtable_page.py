import allure

from ui_tests.dto.dto import Person
from ui_tests.generators.gen_data import generate_person
from ui_tests.locators.elements_page_locators import WebTablePageLocators
from ui_tests.pages.base_page import BasePage


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    @allure.step('Добавление нового пользователя')
    def fill_new_person_form(self, person_info: Person):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(person_info.firstname)
        self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(person_info.lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person_info.email)
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(person_info.age)
        self.element_is_visible(self.locators.SALARY_INPUT).send_keys(person_info.salary)
        self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(person_info.department)
        self.element_is_visible(self.locators.SUBMIT).click()

    @allure.step('Получение всех пользователей из таблицы')
    def get_all_persons_in_table(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return [item.text.splitlines() for item in people_list]

    @allure.step('Поиск пользователя в таблице')
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Редактирование возраста пользователя')
    def update_person_info(self):
        person_info = generate_person()
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()
        return age
