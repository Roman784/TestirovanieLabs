from selenium.webdriver.common.by import By
from base_page import BasePage

class ContactPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "email")
    BIRTHDATE_INPUT = (By.ID, "birthdate")
    PHONE_INPUT = (By.ID, "phone")
    AGREEMENT_CHECKBOX = (By.ID, "agreement")
    SUBMIT_BUTTON = (By.ID, "submitBtn")
    
    # Error messages
    FIRST_NAME_ERROR = (By.ID, "firstNameError")
    LAST_NAME_ERROR = (By.ID, "lastNameError")
    EMAIL_ERROR = (By.ID, "emailError")
    BIRTHDATE_ERROR = (By.ID, "birthdateError")
    AGREEMENT_ERROR = (By.ID, "agreementError")
    
    # Success message
    SUCCESS_MESSAGE = (By.ID, "successMessage")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def load(self, url):
        self.driver.get(url)
    
    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)
    
    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME_INPUT, last_name)
    
    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)
    
    def enter_birthdate(self, birthdate):
        self.send_keys(self.BIRTHDATE_INPUT, birthdate)
    
    def enter_phone(self, phone):
        self.send_keys(self.PHONE_INPUT, phone)
    
    def accept_agreement(self):
        checkbox = self.find_element(self.AGREEMENT_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()
    
    def submit_form(self):
        self.click(self.SUBMIT_BUTTON)
    
    def get_error_message(self, field):
        error_locators = {
            'first_name': self.FIRST_NAME_ERROR,
            'last_name': self.LAST_NAME_ERROR,
            'email': self.EMAIL_ERROR,
            'birthdate': self.BIRTHDATE_ERROR,
            'agreement': self.AGREEMENT_ERROR
        }
        return self.get_text(error_locators[field])
    
    def is_success_message_displayed(self):
        return self.is_element_visible(self.SUCCESS_MESSAGE)
    
    def get_success_message_text(self):
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def fill_all_fields(self, data):
        self.enter_first_name(data['first_name'])
        self.enter_last_name(data['last_name'])
        self.enter_email(data['email'])
        self.enter_birthdate(data['birthdate'])
        self.enter_phone(data.get('phone', ''))
        self.accept_agreement()