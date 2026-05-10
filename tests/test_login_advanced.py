from selenium.webdriver.common.by import By
import time
import os

# Create screenshot folder
os.makedirs("screenshots", exist_ok=True)

# ==================================================
# Test 1
# ==================================================

def test_empty_fields(driver):

    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    time.sleep(2)

    # Click login button
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    time.sleep(2)

    # Read message
    message = driver.find_element(
        By.ID,
        "flash"
    ).text

    print("\nMessage:", message)

    # Save screenshot
    driver.save_screenshot(
        "screenshots/empty_fields.png"
    )

    # Validation
    assert "username is invalid" in message.lower()


# ==================================================
# Test 2
# ==================================================

def test_wrong_credentials(driver):

    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    time.sleep(2)

    # Username
    driver.find_element(
        By.ID,
        "username"
    ).send_keys("wronguser")

    # Password
    driver.find_element(
        By.ID,
        "password"
    ).send_keys("wrongpass")

    # Login click
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    time.sleep(2)

    # Error message
    message = driver.find_element(
        By.ID,
        "flash"
    ).text

    print("\nMessage:", message)

    # Screenshot
    driver.save_screenshot(
        "screenshots/wrong_credentials.png"
    )

    # Validation
    assert "invalid" in message.lower()


# ==================================================
# Test 3
# ==================================================

def test_correct_login(driver):

    driver.get(
        "https://the-internet.herokuapp.com/login"
    )

    time.sleep(2)

    # Correct username
    driver.find_element(
        By.ID,
        "username"
    ).send_keys("tomsmith")

    # Correct password
    driver.find_element(
        By.ID,
        "password"
    ).send_keys("SuperSecretPassword!")

    # Login
    driver.find_element(
        By.CSS_SELECTOR,
        "button[type='submit']"
    ).click()

    time.sleep(2)

    # Screenshot
    driver.save_screenshot(
        "screenshots/correct_login.png"
    )

    print("\nCurrent URL:", driver.current_url)

    # Validation
    assert "secure" in driver.current_url