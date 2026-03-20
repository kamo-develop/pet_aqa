from ui_tests.locators.elements_page_locators import RadioButtonPageLocators
from ui_tests.pages.base_page import BasePage


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_yes_radio_button(self):
        self.element_is_visible(self.locators.YES_LABEL).click()

    def click_on_impressive_radio_button(self):
        self.element_is_visible(self.locators.IMPRESSIVE_LABEL).click()

    def get_disabled_no_radio_button(self):
        return self.element_is_present(self.locators.NO_RADIOBUTTON).get_attribute("disabled")

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text