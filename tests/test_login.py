from pages.login_page import LoginPage
from pages.home_page import HomePage

def test_login(setup):
    driver = setup
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    home = HomePage(driver)

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "Swag Labs" in home.get_title()

