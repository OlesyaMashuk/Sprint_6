from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import allure


class MainPage(BasePage):
    #главная стр
    URL = "https://qa-scooter.education-services.ru/"
    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Закрыть баннер с cookie")
    def close_cookies_popup(self):
        self.click_element(MainPageLocators.BTN_COOKIE_ACCEPT)
        
    
    @allure.step("Клик по вопросу FAQ")
    def click_faq_question(self, index):
        #клик по вопросам
        locator = MainPageLocators.faq_question(index)
        self.scroll_to_element(locator)
        self.click_element(locator)
        
    @allure.step("Получить текст ответа на вопрос FAQ")
    def get_faq_answer_text(self, index):
        #получение текста
        locator = MainPageLocators.faq_answer(index)
        return self.get_text(locator)
    
    @allure.step("Нажать кнопку 'Заказать' хедере")
    def click_order_button_top(self):
        #клик по кнопке Заказать в шапке
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)
    
    @allure.step("Нажать кнопку 'Заказать' в футере")
    def click_order_button_bottom(self):
        #клик по кнопке Заказать внизу стр
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Нажать на логотип Самокат")
    def click_scooter_logo(self):
        #клик по лого самокат
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        #клик по лого Яндекс
        initial_count = self.get_window_count()
        self.click_element(MainPageLocators.YANDEX_LOGO)
        self.wait_for_new_window(initial_count)
        self.switch_to_window_by_index(-1)
        WebDriverWait(self.driver, 10).until(
        lambda d: any(domain in d.current_url for domain in ["ya.ru", "dzen.ru", "yandex.ru"]))