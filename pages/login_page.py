from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self):

        self.driver.get(
            "https://the-internet.herokuapp.com/login"
        )

    def enter_username(self, username):

        self.driver.find_element(
            By.ID,
            "username"
        ).send_keys(username)

    def enter_password(self, password):

        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

    def click_login(self):

        self.driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        ).click()

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()