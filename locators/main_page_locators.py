from selenium.webdriver.common.by import By


class MainPageLocators:
        
    #локаторы для FAQ
    @staticmethod
    def faq_question(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer(index):
        return (By.ID, f"accordion__panel-{index}")
    
    #локаторы для кнопок заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    
    #локаторы для логотипов
    SCOOTER_LOGO = (By.XPATH, "//img[@alt='Scooter']")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")
    BTN_COOKIE_ACCEPT = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")