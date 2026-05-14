import pytest
from drivers.driver_factory import get_driver

@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()
def pytest_html_report_title(report):
    report.title = "Selenium Pytest Automation Report"

