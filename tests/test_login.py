from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.config_reader import read_config


logger = get_logger()


def test_login(setup):

    logger.info("Starting login test")

    driver = setup
    
    config = read_config()

    logger.info("Opening Application")

    driver.get(config["url"])

    login = LoginPage(driver)

    logger.info("Entering credentials")

    login.login("standard_user", "secret_sauce")

    logger.info("Validating title")

    assert "Swag Labs" in driver.title

    logger.info("Login test passed")
