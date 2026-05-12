import os

def take_screenshot(driver, name):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot(f"screenshots/{name}.png")
