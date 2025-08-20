# conftest.py
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.sing_in_page import SignInPage
from selenium.webdriver.chrome.options import Options

import os

# Solo importa ChromeDriverManager si lo vas a usar
if not os.environ.get("GITHUB_ACTIONS"):
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Opcional
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if os.environ.get("GITHUB_ACTIONS"):
        # Crea un directorio temporal único para cada instancia
        user_data_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
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