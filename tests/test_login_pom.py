from pages.login_page import LoginPage

def test_valid_login(driver):

    login = LoginPage(driver)

    login.open()

    login.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    assert "secure" in driver.current_url