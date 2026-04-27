from selenium.webdriver.common.by import By


class MainPageLocators:
    ROOT = [By.ID, "root"]
    APP_ROOT = [By.XPATH, "//div[contains(@class, 'App_App')]"]
    HOME_PAGE = [By.XPATH, "//div[contains(@class, 'Home_HomePage')]"]

    COOKIE_ACCEPT_BUTTON = [By.ID, "rcc-confirm-button"]

    HEADER = [By.XPATH, "//div[contains(@class, 'Header_Header')]"]
    HEADER_SHOW_SEARCH = [By.XPATH, "//div[contains(@class, 'Header_Header')][contains(@class, 'Header_ShowSearch')]"]
    HEADER_LOGO_BLOCK = [By.XPATH, "//div[contains(@class, 'Header_Logo')]"]
    HEADER_DISCLAIMER = [By.XPATH, "//div[contains(@class, 'Header_Disclaimer')]"]
    LOGO_YANDEX = [By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"]
    LOGO_YANDEX_IMG = [By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]//img"]
    LOGO_SCOOTER = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"]
    LOGO_SCOOTER_IMG = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]//img"]

    HEADER_NAV = [By.XPATH, "//div[contains(@class, 'Header_Nav')]"]
    ORDER_BUTTON_TOP = [By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']"]
    ORDER_STATUS_BUTTON = [By.XPATH, "//button[contains(@class, 'Header_Link') and text()='Статус заказа']"]

    ORDER_STATUS_SEARCH_BLOCK = [By.XPATH, "//div[contains(@class, 'Header_SearchInput')]"]
    ORDER_STATUS_INPUT_WRAPPER = [By.XPATH, "//div[contains(@class, 'Header_SearchInput')]//div[contains(@class, 'Input_InputContainer')]"]
    ORDER_NUMBER_INPUT = [By.XPATH, "//div[contains(@class, 'Header_SearchInput')]//input[contains(@class, 'Header_Input')]"]
    ORDER_NUMBER_ERROR = [By.XPATH, "//div[contains(@class, 'Header_SearchInput')]//div[contains(@class, 'Input_ErrorMessage')]"]
    TRACK_ORDER_GO_BUTTON = [By.XPATH, "//div[contains(@class, 'Header_SearchInput')]//button[contains(@class, 'Header_Button')]"]

    HOME_FIRST_PART = [By.XPATH, "//div[contains(@class, 'Home_FirstPart')]"]
    HOME_BLUEPRINT_IMG = [By.XPATH, "//div[contains(@class, 'Home_BluePrint')]//img"]
    HOME_SCOOTER_IMG = [By.XPATH, "//div[contains(@class, 'Home_Scooter')]//img"]
    HOME_ARROW_DOWN = [By.XPATH, "//div[contains(@class, 'Home_ArrowDown')]"]
    HOME_MAIN_HEADLINE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
    HOME_SUBHEADERS = [By.XPATH, "//div[contains(@class, 'Home_Header')]//div[contains(@class, 'Home_SubHeader')]"]

    HOME_TABLE = [By.XPATH, "//div[contains(@class, 'Home_Table')]"]
    HOME_TABLE_ROWS = [By.XPATH, "//div[contains(@class, 'Home_Table')]//div[contains(@class, 'Home_Row')]"]

    HOME_THIRD_PART = [By.XPATH, "//div[contains(@class, 'Home_ThirdPart')]"]
    HOW_IT_WORKS_TITLE = [By.XPATH, "//div[contains(@class, 'Home_ThirdPart')]//div[contains(@class, 'Home_SubHeader')]"]
    HOME_ROADMAP = [By.XPATH, "//div[contains(@class, 'Home_RoadMap')]"]
    ROADMAP_STATUS_BRICKS = [By.XPATH, "//div[contains(@class, 'Home_StatusBrick')]"]
    ORDER_BUTTON_BOTTOM = [By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"]

    HOME_FOUR_PART = [By.XPATH, "//div[contains(@class, 'Home_FourPart')]"]
    FAQ_SECTION_TITLE = [By.XPATH, "//div[contains(@class, 'Home_FourPart')]//div[contains(@class, 'Home_SubHeader')]"]
    HOME_FAQ = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]"]
    ACCORDION_ROOT = [By.XPATH, "//div[contains(@class, 'Home_FAQ')]//div[@data-accordion-component='Accordion']"]

    FAQ_BUTTON_COST = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'Сколько это стоит?')]"]
    FAQ_BUTTON_SEVERAL = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'несколько самокатов')]"]
    FAQ_BUTTON_RENT_TIME = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'Как рассчитывается время аренды?')]"]
    FAQ_BUTTON_TODAY = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'прямо на сегодня')]"]
    FAQ_BUTTON_EXTEND = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'продлить заказ')]"]
    FAQ_BUTTON_CHARGER = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'зарядку вместе с самокатом')]"]
    FAQ_BUTTON_CANCEL = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'отменить заказ')]"]
    FAQ_BUTTON_MKAD = [By.XPATH, "//div[contains(@class, 'accordion__button')][contains(., 'МКАД')]"]

    ACCORDION_HEADING = "//div[@id='accordion__heading-{}']"
    ACCORDION_PANEL = "//div[@id='accordion__panel-{}']"
    ACCORDION_ANSWER_TEXT = [By.TAG_NAME, "p"]
