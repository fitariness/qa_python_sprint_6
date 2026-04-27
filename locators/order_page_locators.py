from selenium.webdriver.common.by import By

ORDER_FORM = "//div[contains(@class, 'Order_Form')]"
ORDER_CONTENT = "//div[contains(@class, 'Order_Content')]"


class OrderPageLocators:
    ORDER_CONTENT_BLOCK = [By.XPATH, ORDER_CONTENT]
    ORDER_STEP_HEADER_WHO = [By.XPATH, "//div[contains(@class, 'Order_Header')][contains(., 'Для кого самокат')]"]
    ORDER_STEP_HEADER_RENT = [By.XPATH, "//div[contains(@class, 'Order_Header')][contains(., 'Про аренду')]"]

    ORDER_FORM_BLOCK = [By.XPATH, "//div[contains(@class, 'Order_Form')]"]

    FIRST_NAME_FIELD = [By.XPATH, f"{ORDER_FORM}//input[contains(@class, 'Input_Responsible')][@placeholder='* Имя']"]
    FIRST_NAME_ERROR = [By.XPATH, f"{ORDER_FORM}//input[@placeholder='* Имя']/following-sibling::div[contains(@class, 'Input_ErrorMessage')]"]
    LAST_NAME_FIELD = [By.XPATH, f"{ORDER_FORM}//input[contains(@class, 'Input_Responsible')][@placeholder='* Фамилия']"]
    LAST_NAME_ERROR = [By.XPATH, f"{ORDER_FORM}//input[@placeholder='* Фамилия']/following-sibling::div[contains(@class, 'Input_ErrorMessage')]"]
    ADDRESS_FIELD = [By.XPATH, f"{ORDER_FORM}//input[contains(@class, 'Input_Responsible')][@placeholder='* Адрес: куда привезти заказ']"]
    ADDRESS_ERROR = [By.XPATH, f"{ORDER_FORM}//input[contains(@placeholder, 'Адрес')]/following-sibling::div[contains(@class, 'Input_ErrorMessage')]"]
    PHONE_FIELD = [By.XPATH, f"{ORDER_FORM}//input[contains(@class, 'Input_Responsible')][@placeholder='* Телефон: на него позвонит курьер']"]
    PHONE_ERROR = [By.XPATH, f"{ORDER_FORM}//input[contains(@placeholder, 'Телефон')]/following-sibling::div[contains(@class, 'Input_ErrorMessage')]"]

    METRO_BLOCK = [By.XPATH, f"{ORDER_FORM}//div[contains(@class, 'select-search')]"]
    METRO_VALUE = [By.XPATH, f"{ORDER_FORM}//div[contains(@class, 'select-search__value')]"]
    METRO_STATION_FIELD = [By.XPATH, f"{ORDER_FORM}//input[contains(@class, 'select-search__input')][@placeholder='* Станция метро']"]

    NEXT_BUTTON_BLOCK = [By.XPATH, "//div[contains(@class, 'Order_NextButton')]"]
    NEXT_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_NextButton')]//button[text()='Далее']"]

    DELIVERY_DATE_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENTAL_PERIOD_DROPDOWN = [By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]"]
    RENTAL_PERIOD_OPTION = "//div[contains(@class, 'Dropdown-option')][normalize-space()='{}']"
    COLOR_BLACK_CHECKBOX = [By.ID, "black"]
    COLOR_GREY_CHECKBOX = [By.ID, "grey"]
    COMMENT_FIELD = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON_MIDDLE = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"]

    CONFIRM_YES_BUTTON = [By.XPATH, "//button[text()='Да']"]
    SUCCESS_MODAL = [By.XPATH, "//*[contains(., 'Заказ оформлен')]"]
