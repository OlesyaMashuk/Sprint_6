import pytest
import allure
from pages.main_page import MainPage
from data.faq_data import FAQData

class TestFAQ:
    # Тесты для раздела 'Вопросы о важном'
    @allure.title("Проверка текстов ответов в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize("question_index", list(range(8)))
    def test_faq_questions(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.open()
        
        #клик на вопрос
        main_page.click_faq_question(question_index)
        
        #получила текст
        actual_answer = main_page.get_faq_answer_text(question_index)
        
        #сравнила с ожиданием
        expected_answer = FAQData.EXPECTED_ANSWERS[question_index]
        assert actual_answer == expected_answer