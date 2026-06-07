import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import locators as loc

class PersonalAccount:
    
    def test_click_through_to_personal_account(self, login, base_url):
        driver = login
        
        # Кликаем "Личный Кабинет"
        driver.find_element(*loc.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        
        # Ждем загрузки страницы профиля
        WebDriverWait(driver, 5).until(
            EC.url_to_be(f"{base_url}/account/profile")
        )
        
        assert driver.current_url == f"{base_url}/account/profile"