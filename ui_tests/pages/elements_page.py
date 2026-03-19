import time

from ui_tests.locators.elements_page_locators import TextBoxPageLocators
from ui_tests.pages.base_page import BasePage


class TextBoxPage(BasePage):

    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Name")
        self.element_is_visible(self.locators.EMAIL).send_keys("email@mail.ru")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("current address")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("perm address")
        self.element_is_visible(self.locators.SUBMIT).click()

    def check_form_submit(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(":")[1]
        assert full_name == "Name"
