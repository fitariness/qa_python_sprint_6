import allure
import pytest

from data import OrderTestData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.browser_base import BaseSeleniumTest


@allure.epic("Самокат")
@allure.feature("Заказ")
@allure.story("Позитивный сценарий")
class TestOrderFlow(BaseSeleniumTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.main_page = MainPage(self.driver)
        self.order_page = OrderPage(self.driver)
        self.main_page.open()
        self.main_page.accept_cookies()

    @allure.title("Заказ самоката: {name} {last_name}")
    @allure.description("Проверяем позитивный сценарий заказа самоката с двумя точками входа")
    @pytest.mark.parametrize(
        "use_top_order_button,name,last_name,address,metro_station,phone,delivery_date,rental_period,color,comment",
        [
            (
                True,
                OrderTestData.USER_TOP["name"],
                OrderTestData.USER_TOP["last_name"],
                OrderTestData.USER_TOP["address"],
                OrderTestData.USER_TOP["metro_station"],
                OrderTestData.USER_TOP["phone"],
                OrderTestData.USER_TOP["delivery_date"],
                OrderTestData.USER_TOP["rental_period"],
                OrderTestData.USER_TOP["color"],
                OrderTestData.USER_TOP["comment"],
            ),
            (
                False,
                OrderTestData.USER_BOTTOM["name"],
                OrderTestData.USER_BOTTOM["last_name"],
                OrderTestData.USER_BOTTOM["address"],
                OrderTestData.USER_BOTTOM["metro_station"],
                OrderTestData.USER_BOTTOM["phone"],
                OrderTestData.USER_BOTTOM["delivery_date"],
                OrderTestData.USER_BOTTOM["rental_period"],
                OrderTestData.USER_BOTTOM["color"],
                OrderTestData.USER_BOTTOM["comment"],
            ),
        ],
        ids=["шапка_иван", "низ_мария"],
    )
    def test_order_scooter_positive_flow(
        self,
        use_top_order_button,
        name,
        last_name,
        address,
        metro_station,
        phone,
        delivery_date,
        rental_period,
        color,
        comment,
    ):
        if use_top_order_button:
            self.main_page.click_order_button_top()
        else:
            self.main_page.click_order_button_bottom()

        assert self.order_page.is_order_page_opened()

        self.order_page.fill_first_step(name, last_name, address, metro_station, phone)
        self.order_page.fill_second_step(delivery_date, rental_period, color, comment)

        assert self.order_page.is_success_modal_displayed()
        assert OrderTestData.SUCCESS_MESSAGE in self.order_page.get_success_message()

        self.main_page.click_scooter_logo()
        assert self.main_page.is_main_page_opened()

        dzen_url = self.main_page.check_yandex_logo_opens_dzen()
        assert "dzen.ru" in dzen_url or "yandex" in dzen_url
