import allure

from ui_tests.locators.elements_page_locators import RadioButtonPageLocators
from ui_tests.pages.base_page import BasePage


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    @allure.step('Клик на радио-кнопку Yes')
    def click_on_yes_radio_button(self):
        self.element_is_visible(self.locators.YES_LABEL).click()

    @allure.step('Клик на радио-кнопку Impressive')
    def click_on_impressive_radio_button(self):
        self.element_is_visible(self.locators.IMPRESSIVE_LABEL).click()

    @allure.step('Получение атрибута disabled для кнопки No')
    def get_disabled_no_radio_button(self):
        return self.element_is_present(self.locators.NO_RADIOBUTTON).get_attribute("disabled")

    @allure.step('Получение результата')
    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text