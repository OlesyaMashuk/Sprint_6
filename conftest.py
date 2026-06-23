
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators 

@pytest.fixture(scope="function")
def driver():
    # Пути к драйверу и браузеру
    driver_path = r"E:\Users\mashukova_ov\Documents\Yandex\Sprint_6\drivers\geckodriver.exe"
    browser_path = r"e:\Users\mashukova_ov\AppData\Local\Mozilla Firefox\firefox.exe"
     
    options = Options()
    options.binary_location = browser_path

    
    service = Service(executable_path=driver_path)
    
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()

@pytest.fixture(autouse=True)
def close_cookies(driver):
    #закрытие кукки
    driver.get("https://qa-scooter.education-services.ru/")
    wait = WebDriverWait(driver, 3)
     
    cookie_button = wait.until(EC.element_to_be_clickable(MainPageLocators.BTN_COOKIE_ACCEPT))
    cookie_button.click()
        
    
    yield