from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

@allure.title("Hola mundo test")
@pytest.mark.smoke
def test_login(pages):
    with allure.step("Navegar a la página principal"):
        pages.home.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        pages.home.click_login()



@pytest.mark.smoke
def test_login2(pages):
    with allure.step("Navegar a la página principal"):
        pages.home.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        pages.home.click_login()



