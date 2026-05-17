import pytest

from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.config_reader import read_config
from utils.excel_utils import get_login_test_data


logger = get_logger()


@pytest.mark.parametrize(
    "username,password",
    get_login_test_data()
)
def test_login(setup, username, password):

    driver = setup

    config = read_config()

    logger.info("Opening application")

    driver.get(config["url"])

    login = LoginPage(driver)

    logger.info(f"Logging in with {username}")

    login.login(username, password)

    assert "Swag Labs" in driver.title
