from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    PERMANENT_ADDRESS = (By.ID, "permanentAddress")
    SUBMIT = (By.ID, "submit")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')


class RadioButtonPageLocators:
    YES_LABEL = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_LABEL = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_LABEL = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    NO_RADIOBUTTON = (By.ID, 'noRadio')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span.text-success')