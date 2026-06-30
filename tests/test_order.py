import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import OrderData

class TestOrder:
    
    @allure.title("Тест оформления заказа через кнопку Заказаьб в хедере")
    def test_order_flow_top_button(self, driver):
        order_data = OrderData.ORDER_SET_TOP
        main_page = MainPage(driver)
        main_page.open()
        
        # клик верхнюю кнопку
        main_page.click_order_button_top()
        
        # заполнение формы 
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        
        order_page.fill_second_form(
            order_data["date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )
        
        #проверка результата
        assert order_page.is_order_success()

    @allure.title("Тест офомления заказа через кнопку Заказать в футере")
    def test_order_flow_bottom_button(self, driver):
        order_data = OrderData.ORDER_SET_BOTTOM
        main_page = MainPage(driver)
        main_page.open()
        
        #клик  нижнюю кнопку
        main_page.click_order_button_bottom()
        
        #заполнение формы
        order_page = OrderPage(driver)
        order_page.fill_first_form(
            order_data["name"],
            order_data["surname"],
            order_data["address"],
            order_data["metro"],
            order_data["phone"]
        )
        
        order_page.fill_second_form(
            order_data["date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )
        
        #проверка результата
        assert order_page.is_order_success()
    
    @allure.title("Тест перехода по клику на лого Самокат")
    def test_scooter_logo_redirect(self, driver):
        #тест клик по лого Самокат
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert OrderData.SCOOTER_EXPECTED_URL in current_url
    
    @allure.title("Тест перехода по клику на лого Яндекс")
    def test_yandex_logo_redirect(self, driver):
        #тест клик по лого Яндекс
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_yandex_logo()
        current_url = main_page.get_current_url()
        is_correct_url = any(d in current_url for d in OrderData.YANDEX_EXPECTED_DOMAINS)
        assert is_correct_url