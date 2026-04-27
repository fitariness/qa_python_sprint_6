import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    @allure.step('Ждём появления элемента на странице')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Ждём когда элемент можно нажать')
    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Ждём когда элемент есть в DOM')
    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Скроллим к элементу по центру экрана')
    def scroll_into_view_center(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element
        )

    @allure.step('Клик через JS')
    def click_js(self, element):
        self.driver.execute_script("arguments[0].click();", element)
