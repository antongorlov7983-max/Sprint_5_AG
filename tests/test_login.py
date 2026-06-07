import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import locators as loc


class TestLogin:

    #Тест входа через разные страницы 
    @pytest.mark.parametrize("url, locator_name", [
        ('https://stellarburgers.education-services.ru/', 'MAIN_PAGE_LOGIN_ACCOUNT_BUTTON'),
        ('https://stellarburgers.education-services.ru/', 'MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON'),
        ('https://stellarburgers.education-services.ru/register', 'REGISTRATION_LOGIN_BUTTON'),
        ('https://stellarburgers.education-services.ru/reset-password', 'PASSWORD_RECOVERY_LOGIN_BUTTON')
    ],
    ids=["main_page",
        "profile_page", 
        "registration_form", 
        "reset-password"
    ])
    def test_multi_page_login(self, driver, existing_user, url, locator_name):
        driver.get(url)

        # Получаем локатор из модуля locators
        locator = getattr(loc, locator_name)
        driver.find_element(*locator).click()

        # Ждем появления формы входа
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(loc.LOGIN_BUTTON))
        # Заполняем форму входа
        driver.find_element(*loc.LOGIN_EMAIL_INPUT).send_keys(existing_user["email"])
        driver.find_element(*loc.LOGIN_PASSWORD_INPUT).send_keys(existing_user["password"])
        driver.find_element(*loc.LOGIN_BUTTON).click()
        # Ждем успешного входа
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(loc.ORDER_BUTTON))
        
        assert driver.find_element(*loc.ORDER_BUTTON).is_displayed()

