from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    
    def fill_first_form(self, name, surname, address, metro, phone):
        #заполнение начальной формы заказа 
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        
        #выбор станции метро
        metro_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_SELECT))
        metro_input.click()
        #time.sleep(0.5)
        metro_option_locator = (By.XPATH, f"//div[contains(text(), '{metro}')]")
        metro_option = self.wait.until(EC.element_to_be_clickable(metro_option_locator))
        metro_option.click()                               
        
        #time.sleep(3)
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        #time.sleep(0.5) 
    
    def fill_second_form(self, date, rental_period, color, comment=""):
        #заполнение второй формы заказа
        #выбор даты
        date_input = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.DATE_INPUT))
        date_input.click()
        #time.sleep(0.5)
        day = date.split('.')[0].lstrip('0')
        locator = (By.XPATH, f"//button[text()='{day}'] | //div[text()='{day}']")
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        #time.sleep(0.5)
        
        
        #выбор срока аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_SELECT)
        #time.sleep(0.5)
        period_option = OrderPageLocators.rental_period_option(rental_period)
        self.click_element(period_option)
        self.driver.execute_script("document.body.click();")
        
        #выбор цвета самоката
        if color == "black":
            self.click_element(OrderPageLocators.SCOOTER_COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.SCOOTER_COLOR_GREY)
            
        
        # Нажать кнопку Заказать
        order_btn = self.wait.until(EC.presence_of_element_located(OrderPageLocators.ORDER_BUTTON))
        self.driver.execute_script("arguments[0].click();", order_btn)
        #time.sleep(3)
        
        # нажат кнопку "Да" в модальном окне
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        #time.sleep(1)
    
    def is_order_success(self):
    #проверка успшного заказа
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MODAL)