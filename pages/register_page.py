
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

    NAME = (By.ID, "name")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm-password")

    REGISTER_BUTTON = (By.ID, "register-button")
    MESSAGE = (By.ID, "message")

    def __init__(self, driver):

        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def enter_name(self, name):
        self.wait.until(
            EC.visibility_of_element_located(self.NAME)
        ).send_keys(name)

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        ).send_keys(email)

    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        ).send_keys(password)

    def enter_confirm_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.CONFIRM_PASSWORD)
        ).send_keys(password)

    def click_register(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REGISTER_BUTTON)
        ).click()

    def get_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MESSAGE)
        ).text
