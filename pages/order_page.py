import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import BASE_URL
from locators.order_page_locators import OrderPageLocators as Loc
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.order_url = f"{BASE_URL}/order"

    def is_order_page_opened(self):
        return self.order_url in self.driver.current_url

    @allure.step('Вводим имя')
    def set_first_name(self, name):
        self.wait_visible(Loc.FIRST_NAME_FIELD).send_keys(name)

    @allure.step('Вводим фамилию')
    def set_last_name(self, last_name):
        self.wait_visible(Loc.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step('Вводим адрес')
    def set_address(self, address):
        self.wait_visible(Loc.ADDRESS_FIELD).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def set_metro_station(self, station):
        metro_input = self.wait_clickable(Loc.METRO_STATION_FIELD)
        metro_input.click()
        metro_input.send_keys(station)
        metro_input.send_keys(Keys.ARROW_DOWN)
        metro_input.send_keys(Keys.ENTER)

    @allure.step('Вводим телефон')
    def set_phone(self, phone):
        self.wait_visible(Loc.PHONE_FIELD).send_keys(phone)

    @allure.step('Кликаем Далее')
    def click_next_button(self):
        self.wait_clickable(Loc.NEXT_BUTTON).click()

    @allure.step('Заполняем первый шаг формы')
    def fill_first_step(self, name, last_name, address, metro_station, phone):
        self.wait_visible(Loc.ORDER_STEP_HEADER_WHO)
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone(phone)
        self.click_next_button()

    @allure.step('Вводим дату доставки')
    def set_delivery_date(self, date):
        date_input = self.wait_visible(Loc.DELIVERY_DATE_FIELD)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды')
    def set_rental_period(self, period):
        self.wait_clickable(Loc.RENTAL_PERIOD_DROPDOWN).click()
        period_option = [By.XPATH, Loc.RENTAL_PERIOD_OPTION.format(period)]
        self.wait_clickable(period_option).click()

    @allure.step('Выбираем цвет самоката')
    def select_scooter_color(self, color):
        if color == "black":
            self.wait_clickable(Loc.COLOR_BLACK_CHECKBOX).click()
        elif color == "grey":
            self.wait_clickable(Loc.COLOR_GREY_CHECKBOX).click()
        else:
            raise ValueError(f"Неизвестный цвет: {color}")

    @allure.step('Вводим комментарий')
    def set_comment(self, comment):
        self.wait_visible(Loc.COMMENT_FIELD).send_keys(comment)

    @allure.step('Кликаем на кнопку Заказать')
    def click_order_button(self):
        self.wait_clickable(Loc.ORDER_BUTTON_MIDDLE).click()

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        self.wait_clickable(Loc.CONFIRM_YES_BUTTON).click()

    @allure.step('Заполняем второй шаг формы')
    def fill_second_step(self, delivery_date, rental_period, color, comment):
        self.wait_visible(Loc.ORDER_STEP_HEADER_RENT)
        self.set_delivery_date(delivery_date)
        self.set_rental_period(rental_period)
        self.select_scooter_color(color)
        self.set_comment(comment)
        self.click_order_button()
        self.confirm_order()

    def is_success_modal_displayed(self):
        return self.wait_visible(Loc.SUCCESS_MODAL).is_displayed()

    def get_success_message(self):
        return self.wait_visible(Loc.SUCCESS_MODAL).text
