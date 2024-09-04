import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    TimeoutException,
    InvalidElementStateException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.by import By
from skraping.chrome_driver import ChromeDriver


class ScrapingUtilities:
    def __init__(
        self,
        website: str,
        web_driver,
        timeout_large: float = 3.0,
        timeout_small: float = 1.0,
        page_load_strategy="none",
    ):
        self.__driver = web_driver(page_load_strategy=page_load_strategy).get_driver()
        self.__timeout_large = timeout_large
        self.__timeout_small = timeout_small
        self.__website = website
        self.__driver.get(self.__website)
        self.__wait = WebDriverWait(self.__driver, self.__timeout_large)

    def click_element(
        self,
        xpath: str,
        error_message: str = "Fel: Det gick inte att klicka på objektet!",
    ) -> bool:
        try:
            element = self.__wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            time.sleep(self.__timeout_small)
            element.click()
            return True
        except InvalidElementStateException:
            print(error_message, "InvalidElementStateException")
        except ElementClickInterceptedException:
            print(error_message, "ElementClickInterceptedException")

        return False

    def click_load_more(self, xpath: str, max_clicks: int = 100) -> None:
        for _ in range(0, max_clicks):
            if not self.click_element(xpath, error_message=""):
                break

    def get_element(
        self, xpath, error_message="FEL: Kunde inte ladda sidelement inom TIMEOUT"
    ):
        try:
            return self.__wait.until(ec.presence_of_element_located((By.XPATH, xpath)))
        except InvalidElementStateException:
            print(error_message)

    def get_element_with_index(self, item_xpath, index, element_xpath):
        xpath = f"{item_xpath}{[index]}{element_xpath}"
        return self.get_element(xpath)

    def get_elements(
        self,
        xpath,
        error_message="FEL: Kunde inte ladda sidelementen inom given TIMEOUT.",
    ):
        try:
            return self.__wait.until(
                ec.presence_of_all_elements_located((By.XPATH, xpath))
            )
        except InvalidElementStateException:
            print(error_message)

    @staticmethod
    def get_text_from_element(element):
        try:
            return element.text
        except NoSuchElementException:
            print("FEL: Inget element hittades")
            return ""

    @staticmethod
    def get_href_from_element(element):
        try:
            return element.get_attribute("href")
        except NoSuchElementException:
            print("FEL: Ingen länk hittades")
            return ""

    def get_driver(self):
        return self.__driver

    def load_page(self, href):
        self.__driver.get(href)
