import time

from ui_tests.pages.elements_page import TextBoxPage


class TestElements:

    class TestTextBox:

        BASE_URL = "https://demoqa.com/text-box"

        def test_correct_filled_text_box(self, driver):
            text_box_page = TextBoxPage(driver, self.BASE_URL)
            text_box_page.open()
            person_info = text_box_page.fill_all_fields_correct_data()
            text_box_page.check_form_correct_submit(person_info)

        def test_incorrect_email_text_box(self, driver):
            text_box_page = TextBoxPage(driver, self.BASE_URL)
            text_box_page.open()
            text_box_page.fill_all_fields_incorrect_email()
            text_box_page.check_incorrect_email()
