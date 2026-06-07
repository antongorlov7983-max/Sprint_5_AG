import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import locators as loc

class TestOpenConstructor:
    @pytest.mark.parametrize('locator_name', [
        'PA_LOGO',
        'PA_DESIGNER_BUTTON'
    ],
    ids=[
        "pass_logo", 
        "pass_button_designer"
    ])
    def test_from_personal_account_to_constructor(self, login, base_url, locator_name):
        driver = login
        
        # Переходим в личный кабинет
        driver.find_element(*loc.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account/profile"))
        
        # Кликаем по конструктору или логотипу
        locator = getattr(loc, locator_name)
        driver.find_element(*locator).click()
        
        # Ждем перехода на главную
        WebDriverWait(driver, 5).until(EC.url_to_be(f"{base_url}/"))
        
        assert driver.current_url == f"{base_url}/"