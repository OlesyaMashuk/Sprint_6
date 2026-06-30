from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Вернуть количество открытых вкладок")
    def get_window_count(self):
        return len(self.driver.window_handles)

    @allure.step("Переключить на вкладку по индексу")
    def switch_to_window_by_index(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step("Ожидание появления нового окна")
    def wait_for_new_window(self, initial_count, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: len(d.window_handles) > initial_count)

    @allure.step("Клик по элементу")
    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ввод текста")
    def send_keys_to_element(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста")
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Проверка видимости элемента")
    def is_element_displayed(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
        
        
    @allure.step("Получение текущего URL")    
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание содержания URL")
    def wait_for_url_contains(self, text, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: text in d.current_url)

    @allure.step("Ждеь изменения URL")
    def wait_url_changed(self, initial_url, timeout=15):
        WebDriverWait(self.driver, timeout).until(lambda d: d.current_url != initial_url)

    @allure.step("Ожидание выполнения условия")
    def wait_until(self, condition_func, timeout=10):
        WebDriverWait(self.driver, timeout).until(condition_func)    

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, locator):
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            return element
        