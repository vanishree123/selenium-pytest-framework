import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox", "edge"])
def setup(request):

    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise Exception("Browser not supported")

    driver.maximize_window()

    yield driver

    driver.quit()

