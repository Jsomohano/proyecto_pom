from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

class HomePage(BasePage):

    #Locators
    login_button = (By.CLASS_NAME, "user-info")
    register_button = (By.XPATH, "//[@class='blockcart cart-preview inactive']")

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(__name__)

    def click_login(self):
        self.logger.info("Haciendo click en el botón de login")
        self.click_element(self.login_button)

    def click_register(self):
        self.logger.info("Haciendo click en el botón de registro")
        self.click_element(self.register_button)

    def navigate_to_home_page(self):
        self.logger.info("Navegando a la página principal")
        self.driver.get("https://teststore.automationtesting.co.uk/index.php")
        self.logger.info("Página principal cargada exitosamente")