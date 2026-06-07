from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as loc


class TestRegistration:
    
    # Успешная регистрация
    def test_successful_registration(self, driver, base_url):
        import random
        import string
        
        name = "Тестовый Пользователь"
        digits = ''.join(random.choices(string.digits, k=3))
        email = f"Anton_Gorlov_42_{digits}@ya.ru"
        password = "123456"  # 6 символов
        
        driver.get(f"{base_url}/register")
        
        driver.find_element(*loc.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*loc.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*loc.REGISTRATION_PASSWORD).send_keys(password)
        driver.find_element(*loc.REGISTRATION_BUTTON).click()
        
        WebDriverWait(driver, 5).until(
            EC.url_to_be(f"{base_url}/login")
        )
        
       
        assert driver.current_url == f"{base_url}/login"
    
    # Тест ошибки при пароле менее 6 символов
    def test_registration_invalid_password(self, driver, base_url):
        name = "Тестовый Пользователь"
        email = "test@ya.ru"
        invalid_password = "12345" 
        
        driver.get(f"{base_url}/register")
        
        driver.find_element(*loc.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*loc.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*loc.REGISTRATION_PASSWORD).send_keys(invalid_password)
        driver.find_element(*loc.REGISTRATION_BUTTON).click()
        
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(loc.REGISTRATION_PASSWORD_ERROR)
        )
        
        assert "Некорректный пароль" in error_message.text