import time

from ui_tests.generators.gen_data import generate_person
from ui_tests.pages.elements_page import TextBoxPage


class TestElements:

    class TestTextBox:

        BASE_URL = "https://demoqa.com/text-box"

        def test_correct_filled_text_box(self, driver):
            person_info = generate_person()
            text_box_page = TextBoxPage(driver, self.BASE_URL)
            text_box_page.open()
            text_box_page.fill_form(person_info)
            created_person = text_box_page.get_created_person_data()

            assert person_info == created_person

        def test_incorrect_email_text_box(self, driver):
            person_info = generate_person()
            person_info.email = "wrong_email"

            text_box_page = TextBoxPage(driver, self.BASE_URL)
            text_box_page.open()
            text_box_page.fill_form(person_info)
            assert "field-error" in text_box_page.get_email_input_classes()
