from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.sing_in_page import SignInPage
import pytest
import allure
from utils.logger import get_logger
logger = get_logger(__name__)


logger = get_logger(__name__)
@allure.title("Hola mundo test")
@pytest.mark.smoke
def test_login(driver):
    home_page = HomePage(driver)
    sign_in_page = SignInPage(driver)

    with allure.step("Navegar a la página principal"):
        logger.info("Navegando a la página principal")
        allure.attach("Navegando a la página principal", name="Step Info", attachment_type=allure.attachment_type.TEXT)
        home_page.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        logger.info("Click en login")
        allure.attach("Click en login", name="Step Info", attachment_type=allure.attachment_type.TEXT)
        home_page.click_login()



@pytest.mark.smoke
def test_login2(driver):
    home_page = HomePage(driver)
    sign_in_page = SignInPage(driver)

    with allure.step("Navegar a la página principal"):
        logger.info("Navegando a la página principal")
        allure.attach("Navegando a la página principal", name="Step Info", attachment_type=allure.attachment_type.TEXT)
        home_page.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        logger.info("Click en login")
        allure.attach("Click en login", name="Step Info", attachment_type=allure.attachment_type.TEXT)
        home_page.click_login()



