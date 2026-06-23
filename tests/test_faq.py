import pytest
from pages.main_page import MainPage
from data.faq_data import FAQData


class TestFAQ:
    #Тесты для раздела 'Вопросы о важном'
    
    def test_faq_question_0(self, driver):
        #тест вопроса_0
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(0)
        actual_answer = main_page.get_faq_answer_text(0)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[0]
    
    def test_faq_question_1(self, driver):
        #тест вопроса_1
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(1)
        actual_answer = main_page.get_faq_answer_text(1)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[1]
    
    def test_faq_question_2(self, driver):
        #тест вопроса_2
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(2)
        actual_answer = main_page.get_faq_answer_text(2)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[2]
    
    def test_faq_question_3(self, driver):
        #тест вопроса_3
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(3)
        actual_answer = main_page.get_faq_answer_text(3)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[3]
    
    def test_faq_question_4(self, driver):
        #тест вопроса_4
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(4)
        actual_answer = main_page.get_faq_answer_text(4)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[4]
    
    def test_faq_question_5(self, driver):
        #тест вопроса_5
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(5)
        actual_answer = main_page.get_faq_answer_text(5)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[5]
    
    def test_faq_question_6(self, driver):
        #тест вопроса_6
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(6)
        actual_answer = main_page.get_faq_answer_text(6)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[6]
    
    def test_faq_question_7(self, driver):
        #тест вопроса_7
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_faq_question(7)
        actual_answer = main_page.get_faq_answer_text(7)
        assert actual_answer == FAQData.EXPECTED_ANSWERS[7]