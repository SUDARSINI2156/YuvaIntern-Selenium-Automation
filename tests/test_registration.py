
import pytest

from pages.register_page import RegisterPage
from utils.config import BASE_URL
from utils.logger import logger
from utils.test_data import registration_data


def test_registration_page_title(driver):

    logger.info("Starting registration page title test")

    page = RegisterPage(driver)
    page.open_page(BASE_URL)

    assert "Student Registration" in driver.title

    logger.info("Registration page title test passed")


def test_successful_registration(driver):

    logger.info("Starting successful registration test")

    data = registration_data[0]

    page = RegisterPage(driver)
    page.open_page(BASE_URL)

    page.enter_name(data["name"])
    page.enter_email(data["email"])
    page.enter_password(data["password"])
    page.enter_confirm_password(data["confirm_password"])

    page.click_register()

    message = page.get_message()

    assert "success" in message.lower()

    logger.info("Successful registration test passed")


def test_password_mismatch(driver):

    logger.info("Starting password mismatch test")

    data = registration_data[1]

    page = RegisterPage(driver)
    page.open_page(BASE_URL)

    page.enter_name(data["name"])
    page.enter_email(data["email"])
    page.enter_password(data["password"])
    page.enter_confirm_password(data["confirm_password"])

    page.click_register()

    message = page.get_message()

    assert "match" in message.lower()

    logger.info("Password mismatch test passed")
