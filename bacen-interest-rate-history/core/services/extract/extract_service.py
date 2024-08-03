import time
from io import StringIO
from typing import Tuple

import pandas as pd
from interfaces.i_extract_service import IExtractService
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.web_driver import WebDriver


class ExtractService(IExtractService):
    def __init__(self) -> None:
        self.web_driver = WebDriver()

    def extract_data(self) -> Tuple[pd.DataFrame, str, bool]:
        browser = None
        message = "Extração realizada com sucesso."

        try:
            browser = self.web_driver.get_browser()
            browser.get("https://www.bcb.gov.br/controleinflacao/historicotaxasjuros")

            time.sleep(50)

            wait = WebDriverWait(browser, 100)
            wait.until(
                lambda browser: browser.execute_script("return document.readyState")
                == "complete"
            )

            xpath = wait.until(
                EC.visibility_of_element_located(
                    (
                        By.XPATH,
                        "/html/body/app-root/app-root/div/div/main/dynamic-comp/div/div/bcb-histtaxajuros/div[1]/table",
                    )
                )
            )

            table_html = xpath.get_attribute("outerHTML")
            data = pd.read_html(StringIO(table_html))[0]

            if data.empty or data is None:
                return pd.DataFrame(), "DataFrame vazio.", False
            else:
                return data, message, True

        except TimeoutException:
            message = "Elemento não foi encontrado."
            return pd.DataFrame(), message, False

        except Exception as e:
            message = f"Ocorreu um erro: {str(e)}"
            return pd.DataFrame(), message, False

        finally:
            if browser:
                browser.quit()
