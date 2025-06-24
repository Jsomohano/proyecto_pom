# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.sing_in_page import SignInPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    """Fixture que proporciona una instancia de HomePage ya configurada"""
    return HomePage(driver)

@pytest.fixture
def sign_in_page(driver):
    """Fixture que proporciona una instancia de SignInPage ya configurada"""
    return SignInPage(driver)

@pytest.fixture
def pages(driver):
    """
    Fixture que proporciona todas las páginas instanciadas en un solo objeto.
    Uso: def test_example(pages):
        pages.home.navigate_to_home_page()
        pages.sign_in.enter_sign_in_info(email, password)
    """
    class Pages:
        def __init__(self, driver):
            self.home = HomePage(driver)
            self.sign_in = SignInPage(driver)
    
    return Pages(driver)