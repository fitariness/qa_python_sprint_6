import allure
import pytest

from pages.main_page import MainPage
from tests.browser_base import BaseSeleniumTest


@allure.epic("Самокат")
@allure.feature("Главная")
@allure.story("FAQ")
class TestFaqSection(BaseSeleniumTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        # создаем объект главной страницы
        self.main_page = MainPage(self.driver)
        self.main_page.open()
        self.main_page.accept_cookies()

    @allure.title("FAQ вопрос {question_index}")
    @allure.description("Проверяем, что после клика по вопросу показывается ожидаемый фрагмент ответа")
    @pytest.mark.parametrize(
        "question_index,expected_text",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат"),
            (2, "Мы привозим самокат 8 мая в течение дня"),
            (3, "Только начиная с завтрашнего дня"),
            (4, "Пока что нет! Но если что-то срочное"),
            (5, "Этого хватает на восемь суток"),
            (6, "Да, пока самокат не привезли"),
            (7, "Да, обязательно. Всем самокатов!"),
        ],
        ids=[
            "вопрос_0_цена",
            "вопрос_1_несколько",
            "вопрос_2_время_аренды",
            "вопрос_3_сегодня",
            "вопрос_4_продлить",
            "вопрос_5_зарядка",
            "вопрос_6_отмена",
            "вопрос_7_мкад",
        ],
    )
    def test_faq_accordion_opens_correct_answer(self, question_index, expected_text):
        # кликаем на вопрос
        self.main_page.click_faq_question(question_index)
        # получаем текст ответа
        actual_text = self.main_page.get_faq_answer_text(question_index)
        # проверяем что нужный текст есть в ответе
        assert expected_text in actual_text
