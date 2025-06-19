from .base_page import BasePage
from selenium.webdriver.common.by import By

class SignInPage(BasePage):
    email_field = By.CLASS_NAME,"ADS"
    password_field = By.CLASS_NAME,"ADS"
    submit_btn = By.CLASS_NAME,"ADS"
    #Locators
    login_button = (By.CLASS_NAME, "user-info")
    register_button = (By.XPATH, "//[@class='blockcart cart-preview inactive']")

    def __init__(self, driver):
        super().__init__(driver)

    def enter_sign_in_info(self, email, password):
        self.enter_text(self.email_field, email)
        self.enter_text(self.password_field, password)
        self.click_element(self.submit_btn)