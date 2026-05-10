from selenium.webdriver.common.by import By
import time

# ==================================================
# Test 1 — Empty Login
# ==================================================
def test_empty_fields(driver):          # ← added 'driver' here
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    print("\nMessage:", message)
    assert "username is invalid" in message.lower()

# ==================================================
# Test 2 — Wrong Credentials
# ==================================================
def test_wrong_credentials(driver):     # ← added 'driver' here
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text
    print("\nMessage:", message)
    assert "invalid" in message.lower()

# ==================================================
# Test 3 — Correct Login
# ==================================================
def test_correct_login(driver):         # ← added 'driver' here
    driver.get("https://the-internet.herokuapp.com/login")
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)
    assert "secure" in driver.current_url
    print("\nLogin Successful")