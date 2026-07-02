import os
import pytest
from selenium import webdriver
from pytest_html import extras

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on"
    )

@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":

        from selenium.webdriver.chrome.options import Options

        chrome_options = Options()

        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":

        driver = webdriver.Firefox()

    elif browser == "edge":

        driver = webdriver.Edge()

    else:

        raise Exception("Browser not supported")

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:

        driver = item.funcargs["setup"]

        screenshots_dir = "screenshots"

        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)

        file_name = f"{item.name}.png"

        screenshot_path = os.path.join(
            screenshots_dir,
            file_name
        )

        driver.save_screenshot(screenshot_path)

        extra.append(
            extras.image(screenshot_path)
        )

    report.extra = extra


def pytest_html_report_title(report):
    report.title = "Selenium Pytest Automation Report"
