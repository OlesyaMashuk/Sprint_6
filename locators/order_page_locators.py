from selenium.webdriver.common.by import By


class OrderPageLocators:
        
    # Локатор формы (Для кого самокат)
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_SELECT = (By.CLASS_NAME, "select-search")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Локатор  формы (Про аренду)
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_SELECT = (By.XPATH, "//div[text()='* Срок аренды']")
    SCOOTER_COLOR_BLACK = (By.ID, "black")
    SCOOTER_COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__1xGrp')]//button[contains(text(), 'Заказать')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[text()='Да']")
    METRO_OPTIONS_LIST = (By.XPATH, "//div[contains(@class, 'select-search__value')]")
    
    # Локатор для модального окна успеха
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']")
    
    @staticmethod
    def metro_option(metro):
        # Локатор для выбора станции М
        return (By.XPATH, f"//div[contains(text(), '{metro}')]")
    
    @staticmethod
    def rental_period_option(period):
        # Локатор для выбора даты
        return (By.XPATH, f"//div[text()='{period}']")
    
    @staticmethod
    def date_option(day):
        #локатор для конкретного дня в календаре
        return (By.XPATH, f"//button[text()='{day}'] | //div[text()='{day}']")