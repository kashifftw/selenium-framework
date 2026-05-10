from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # ← this line hides the browser
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()