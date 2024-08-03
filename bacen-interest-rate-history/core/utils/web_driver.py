from config.selenium_config import get_chrome_options
from selenium import webdriver


class WebDriver:
    def __init__(self):
        self.options = get_chrome_options()

    def get_browser(self) -> webdriver.Chrome:
        return webdriver.Chrome(options=self.options)
