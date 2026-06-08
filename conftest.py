import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as loc


@pytest.fixture(scope="function")
def driver():
    """Фикстура драйвера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def base_url():
    """Базовый URL"""
    return 'https://stellarburgers.education-services.ru'


@pytest.fixture(scope="function")
def existing_user():
    """Существующий пользователь"""
    return {
        'email': 'Anton_Gorlov_42_456@ya.ru',
        'password': '123456'
    }


@pytest.fixture(scope="function")
def login(driver, base_url, existing_user):
    """Авторизованный пользователь"""
    driver.get(f"{base_url}/login")
    
    wait = WebDriverWait(driver, 5)
    wait.until(EC.element_to_be_clickable(loc.LOGIN_BUTTON))
    
    driver.find_element(*loc.LOGIN_EMAIL_INPUT).send_keys(existing_user["email"])
    driver.find_element(*loc.LOGIN_PASSWORD_INPUT).send_keys(existing_user["password"])
    driver.find_element(*loc.LOGIN_BUTTON).click()
    
    wait.until(EC.visibility_of_element_located(loc.ORDER_BUTTON))
    
    yield driver