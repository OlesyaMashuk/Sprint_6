import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import OrderData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrder:
    #тест позитивного сценария с разными точками входа (две кнопки "заказать")
    @pytest.mark.parametrize("order_data, button_method", [
        (OrderData.ORDER_SET_TOP, "top"),
        (OrderData.ORDER_SET_BOTTOM, "bottom")
    ], ids=["top_button", "bottom_button"])
    def test_order_flow(self, driver, order_data, button_method):
        main_page = MainPage(driver)
        main_page.open()
        
        #выбор кнопки в зависимости от метода
        if button_method == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()
        
        #заполнить форму заказа
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
        
        #проверить появление успешного заказа
        assert order_page.is_order_success()
    
    def test_scooter_logo_redirect(self, driver):
        #тест клик по лого Самокат
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert OrderData.SCOOTER_EXPECTED_URL in current_url
    
    def test_yandex_logo_redirect(self, driver):
        #тест клик по лого Яндекс
        main_page = MainPage(driver)
        main_page.open()
        windows_count_before = len(driver.window_handles)
        main_page.click_yandex_logo()
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > windows_count_before)
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 15).until(
        lambda d: d.current_url != "about:blank")
        current_url = driver.current_url
        is_correct_url = any(d in current_url for d in OrderData.YANDEX_EXPECTED_DOMAINS)
        assert is_correct_url, f"Неверный URL! Ожидали один из {OrderData.YANDEX_EXPECTED_DOMAINS}, но получили: {current_url}"