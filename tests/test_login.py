from pages.login_page import LoginPage
from utils.screenshot import take_screenshot

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    take_screenshot(driver, "login_success")

    assert "Swag Labs" in driver.title
