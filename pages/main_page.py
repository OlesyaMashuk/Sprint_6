from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    #главная стр
    
    URL = "https://qa-scooter.education-services.ru/"
    def open(self):
        self.driver.get(self.URL)
    
    def click_faq_question(self, index):
        #клик по вопросам
        locator = MainPageLocators.faq_question(index)
        self.click_element(locator)
        #import time
        #time.sleep(0.5)
    
    def get_faq_answer_text(self, index):
        #получение текста
        locator = MainPageLocators.faq_answer(index)
        return self.get_text(locator)
    
    def click_order_button_top(self):
        #клик по кнопке Заказать в шапке
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    def click_order_button_bottom(self):
        #клик по кнопке Заказать внизу стр
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    def click_scooter_logo(self):
        #клик по лого самокат
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    def click_yandex_logo(self):
        #клик по лого Яндекс
        self.click_element(MainPageLocators.YANDEX_LOGO)
        self.switch_to_new_window()