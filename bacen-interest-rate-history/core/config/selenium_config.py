from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return options