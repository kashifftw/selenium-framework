from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_explicit_wait(driver):

    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "username")
        )
    )

    username.send_keys("tomsmith")

    password = driver.find_element(
        By.ID,
        "password"
    )

    password.send_keys(
        "SuperSecretPassword!"
    )

    login_btn = driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

    login_btn.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("secure")
    )

    assert "secure" in driver.current_url