from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from config import IMPLICIT_WAIT


class BaseSeleniumTest:
    driver = None

    @classmethod
    def setup_class(cls):
        # инициализируем драйвер Firefox
        service = Service(GeckoDriverManager().install())
        cls.driver = webdriver.Firefox(service=service)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(IMPLICIT_WAIT)

    @classmethod
    def teardown_class(cls):
        # закрываем браузер после выполнения тестов
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None
