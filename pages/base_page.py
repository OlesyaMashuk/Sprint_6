from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def click_element(self, locator):
        # Клик по элементу с ожиданием
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except ElementClickInterceptedException:
            #прокрутка если нужна
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            
            try:
                element.click()
            except ElementClickInterceptedException:
                #через JavaScript
                self.driver.execute_script("arguments[0].click();", element)
    
    def send_keys_to_element(self, locator, text):
        #ввод текста
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except TimeoutException:
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(text)
    
    def get_text(self, locator):
        #получение текста
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            element = self.driver.find_element(*locator)
            return element.text
    
    def is_element_displayed(self, locator):
        #видимость элеимента
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except (TimeoutException, NoSuchElementException):
            return False
    
    def switch_to_new_window(self):
        #переключение на новую вкладку
        try:
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except IndexError:
            pass
    
    def get_current_url(self):
        #получение URL
        return self.driver.current_url
    
    def scroll_to_element(self, locator):
        #прокрутка до элемента
        try:
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            time.sleep(0.5)
            return element
        except NoSuchElementException:
             return None