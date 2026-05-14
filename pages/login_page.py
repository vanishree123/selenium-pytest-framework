from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def login(self, user, pwd):

        self.enter_text(self.username, user)

        self.enter_text(self.password, pwd)

        self.click(self.login_btn)

