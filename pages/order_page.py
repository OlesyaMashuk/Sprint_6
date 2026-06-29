import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators



class OrderPage(BasePage):
    @allure.step("Заполнить первую форму заказа")
    def fill_first_form(self, name, surname, address, metro, phone):
        #заполнение начальной формы заказа 
        self.send_keys_to_element(OrderPageLocators.NAME_INPUT, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_INPUT, address)
        
        #выбор станции метро
        self.click_element(OrderPageLocators.METRO_SELECT)
        option_locator = OrderPageLocators.metro_option(metro)
        self.click_element(option_locator)

                                     
        #заполню телефон
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
        self.click_element(OrderPageLocators.NEXT_BUTTON)
         
    @allure.step("Заполнить вторую форму заказа")
    def fill_second_form(self, date, rental_period, color, comment=""):
        #заполнение второй формы заказа
        #выбор даты
        self.click_element(OrderPageLocators.DATE_INPUT)    
        day = date.split('.')[0].lstrip('0')
        day_locator = OrderPageLocators.date_option(day)
        self.click_element(day_locator)
                        
        #выбор срока аренды
        self.click_element(OrderPageLocators.RENTAL_PERIOD_SELECT)
        period_option = OrderPageLocators.rental_period_option(rental_period)
        self.click_element(period_option)
        
        
        #выбор цвета самоката
        if color == "black":
            self.click_element(OrderPageLocators.SCOOTER_COLOR_BLACK)
        elif color == "grey":
            self.click_element(OrderPageLocators.SCOOTER_COLOR_GREY)
            
        
        # Нажать кнопку Заказать
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        
        # нажат кнопку "Да" в модальном окне
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        
    @allure.step("Проверить успешность заказа")
    def is_order_success(self):
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MODAL)