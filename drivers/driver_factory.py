from selenium import webdriver
from utils.config_reader import read_config


def get_driver():

    config = read_config()

    browser = config["browser"].lower()

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    else:
        raise Exception("Browser not supported")

    driver.maximize_window()

    return driver
