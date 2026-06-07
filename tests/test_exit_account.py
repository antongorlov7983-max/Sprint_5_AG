import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import locators as loc

class TestExitAccount:
     def test_exit_account(self, login):
        driver = login
        
        # Переходим в личный кабинет
        driver.find_element(*loc.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains("/account/profile"))
        
        # Нажимаем кнопку "Выход"
        driver.find_element(*loc.LOGOUT_BUTTON).click()
        
        # Проверяем, что перебросило на страницу логина
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        
        # Проверяем заголовок "Вход"
        login_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//h2[contains(text(),"Вход")]'))
        )
        assert "Вход" in login_header.text