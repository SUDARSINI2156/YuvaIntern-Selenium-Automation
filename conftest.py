
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config import HEADLESS


@pytest.fixture
def driver():

    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument("--window-size=1365,900")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)

    try:
        yield browser

    finally:
        browser.quit()
