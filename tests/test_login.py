from pages.login_page import LoginPage
from utils.logger import get_logger


logger = get_logger()


def test_login(setup):

    logger.info("Starting login test")

    driver = setup

    logger.info("Opening SauceDemo website")

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)

    logger.info("Entering credentials")

    login.login("standard_user", "secret_sauce")

    logger.info("Validating title")

    assert "Swag Labs" in driver.title

    logger.info("Login test passed")
