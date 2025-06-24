from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

class SignInPage(BasePage):
    email_field = By.CLASS_NAME,"ADS"
    password_field = By.CLASS_NAME,"ADS"
    submit_btn = By.CLASS_NAME,"ADS"
    #Locators
    login_button = (By.CLASS_NAME, "user-info")
    register_button = (By.XPATH, "//[@class='blockcart cart-preview inactive']")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(__name__)

    def enter_sign_in_info(self, email, password):
        self.logger.info(f"Llenando formulario de login con email: {email}")
        self.enter_text(self.email_field, email)
        self.enter_text(self.password_field, password)
        self.logger.info("Haciendo click en el botón de submit")
        self.click_element(self.submit_btn)