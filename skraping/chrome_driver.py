from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
    def __init__(self, page_load_strategy='none', arguments=None,
                 maximized_window=True):
        if arguments is None:
            arguments = ["--disable-search-engine-choice-screen"]
        self.__options = Options()
        self.__options.page_load_strategy = page_load_strategy
        for argument in arguments:
            self.__options.add_argument(argument)
        self.__driver = webdriver.Chrome(options=self.__options, service=ChromeService(ChromeDriverManager().install()))
        if maximized_window:
            self.__driver.maximize_window()

    def get_driver(self) -> webdriver:
        return self.__driver
