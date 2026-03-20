import allure

from ui_tests.pages.radiobutton_page import RadioButtonPage


@allure.feature('RadioButton')
class TestRadioButton:
    BASE_URL = "https://demoqa.com/radio-button"

    @allure.title('Проверка нажатия на радио-кнопку Yes')
    def test_yes_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, self.BASE_URL)
        radio_button_page.open()
        radio_button_page.click_on_yes_radio_button()
        output_result = radio_button_page.get_output_result()
        assert output_result == "Yes"

    @allure.title('Проверка нажатия на радио-кнопку Impressive')
    def test_impressive_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, self.BASE_URL)
        radio_button_page.open()
        radio_button_page.click_on_impressive_radio_button()
        output_result = radio_button_page.get_output_result()
        assert output_result == "Impressive"

    @allure.title('Кнопка No отключена')
    def test_no_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, self.BASE_URL)
        radio_button_page.open()
        disabled = radio_button_page.get_disabled_no_radio_button()
        assert disabled == "true"