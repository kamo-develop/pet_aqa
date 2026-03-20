import allure

from ui_tests.dto.dto import Person
from ui_tests.locators.elements_page_locators import TextBoxPageLocators
from ui_tests.pages.base_page import BasePage


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    @allure.step('Заполнение поля Full Name')
    def fill_full_name(self, person_info: Person):
        self.element_is_visible(self.locators.FULL_NAME).send_keys(person_info.full_name)

    @allure.step('Заполнение поля Email')
    def fill_email(self, person_info: Person):
        self.element_is_visible(self.locators.EMAIL).send_keys(person_info.email)

    @allure.step('Заполнение поля Current Address')
    def fill_current_address(self, person_info: Person):
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person_info.current_address)

    @allure.step('Заполнение поля Permanent Address')
    def fill_permanent_address(self, person_info: Person):
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(person_info.permanent_address)

    @allure.step('Клик по кнопке отправки формы')
    def click_submit_button(self):
        self.element_is_clickable(self.locators.SUBMIT).click()

    @allure.step('Заполнение формы')
    def fill_form(self, person: Person):
        self.fill_full_name(person)
        self.fill_email(person)
        self.fill_current_address(person)
        self.fill_permanent_address(person)
        self.click_submit_button()

    @allure.step('Получение css класса для поля Email')
    def get_email_input_classes(self):
        return self.element_is_visible(self.locators.EMAIL).get_attribute("class")

    @allure.step('Получение созданного пользователя')
    def get_created_person_data(self):
        return Person(
            full_name=self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1].strip(),
            email=self.element_is_present(self.locators.CREATED_EMAIL).text.split(":")[1].strip(),
            current_address=self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1].strip(),
            permanent_address=self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1].strip(),
        )
