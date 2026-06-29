import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from pages.main_page import MainPage

@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get("https://qa-scooter.education-services.ru/")

    yield driver

    driver.quit()

@pytest.fixture(autouse=True)
def close_cookies(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.close_cookies_popup()
    yield