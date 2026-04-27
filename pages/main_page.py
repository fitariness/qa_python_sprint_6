import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, EXTERNAL_PAGE_WAIT
from locators.main_page_locators import MainPageLocators as Loc
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = BASE_URL

    @allure.step('Открываем главную страницу')
    def open(self):
        self.driver.get(self.base_url)

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        try:
            cookie_button = self.wait_clickable(Loc.COOKIE_ACCEPT_BUTTON)
            cookie_button.click()
        except TimeoutException:
            pass

    @allure.step('Кликаем на верхнюю кнопку Заказать')
    def click_order_button_top(self):
        self.wait_clickable(Loc.ORDER_BUTTON_TOP).click()

    @allure.step('Кликаем на нижнюю кнопку Заказать')
    def click_order_button_bottom(self):
        bottom_button = self.wait_clickable(Loc.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView();", bottom_button)
        bottom_button.click()

    @allure.step('Кликаем на вопрос FAQ')
    def click_faq_question(self, question_index):
        locator = [By.XPATH, Loc.ACCORDION_HEADING.format(question_index)]
        question = self.wait_present(locator)
        self.scroll_into_view_center(question)
        self.click_js(question)

    @allure.step('Получаем текст ответа FAQ')
    def get_faq_answer_text(self, question_index):
        panel_locator = [By.XPATH, Loc.ACCORDION_PANEL.format(question_index)]
        panel = self.wait_visible(panel_locator)
        answer_text = panel.find_element(*Loc.ACCORDION_ANSWER_TEXT).text
        return answer_text

    @allure.step('Кликаем на логотип Самоката')
    def click_scooter_logo(self):
        logo = self.wait_present(Loc.LOGO_SCOOTER)
        self.scroll_into_view_center(logo)
        self.click_js(logo)

    @allure.step('Кликаем на логотип Яндекса')
    def click_yandex_logo(self):
        self.wait_clickable(Loc.LOGO_YANDEX).click()

    def is_main_page_opened(self):
        current = self.driver.current_url.rstrip("/")
        base = self.base_url.rstrip("/")
        return current == base

    @allure.step('Проверяем переход на Дзен в новой вкладке')
    def check_yandex_logo_opens_dzen(self):
        original_window = self.driver.current_window_handle
        new_handle = None
        self.click_yandex_logo()
        self.wait.until(lambda d: len(d.window_handles) > 1)

        for handle in self.driver.window_handles:
            if handle != original_window:
                new_handle = handle
                self.driver.switch_to.window(handle)
                break
        try:
            WebDriverWait(self.driver, EXTERNAL_PAGE_WAIT).until(
                lambda d: "dzen.ru" in d.current_url or "yandex" in d.current_url.lower()
            )
            return self.driver.current_url.lower()
        finally:
            if new_handle and new_handle in self.driver.window_handles:
                self.driver.close()
            self.driver.switch_to.window(original_window)
