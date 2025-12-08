import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pages.contact_page import ContactPage

class TestContactForm:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        html_file_path = f"file://{os.path.join(current_dir, '..', 'index.html')}"
        
        self.contact_page = ContactPage(self.driver)
        self.contact_page.load(html_file_path)
        
        yield
        
        self.driver.quit()
    
    def test_positive_submit_form_with_valid_data(self):
        test_data = {
            'first_name': 'Иван',
            'last_name': 'Петров',
            'email': 'ivan.petrov@example.com',
            'birthdate': '10-10-1990',
            'phone': '+7 (999) 123-45-67',
        }
        
        self.contact_page.fill_all_fields(test_data)
        
        self.contact_page.submit_form()
        
        assert self.contact_page.is_success_message_displayed(), "Сообщение об успехе не отображается"
        
        success_text = self.contact_page.get_success_message_text()
        expected_text = "Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время."
        assert success_text == expected_text, f"Ожидался текст: {expected_text}, но получен: {success_text}"
    
    def test_negative_submit_form_with_empty_required_field(self):
        self.contact_page.enter_first_name('Иван')
        self.contact_page.enter_last_name('Петров')
        self.contact_page.enter_email('ivan@example.com')
        self.contact_page.enter_phone('+7 (999) 123-45-67')
        self.contact_page.accept_agreement()
        
        self.contact_page.submit_form()
        
        error_message = self.contact_page.get_error_message('birthdate')
        expected_error = "Поле обязательно для заполнения"
        assert error_message == expected_error, f"Ожидалась ошибка: {expected_error}, но получена: {error_message}"
        
        assert not self.contact_page.is_success_message_displayed(), "Сообщение об успехе не должно отображаться при ошибках"
    
    def test_negative_submit_form_with_underage_user(self):
        test_data = {
            'first_name': 'Иван',
            'last_name': 'Петров',
            'email': 'ivan.petrov@example.com',
            'birthdate': '01-01-2010',
            'phone': '+7 (999) 123-45-67',
        }
        
        self.contact_page.fill_all_fields(test_data)
        self.contact_page.submit_form()
        
        error_message = self.contact_page.get_error_message('birthdate')
        expected_error = "Регистрация разрешена с 18 лет"
        assert error_message == expected_error, f"Ожидалась ошибка: {expected_error}, но получена: {error_message}"
    