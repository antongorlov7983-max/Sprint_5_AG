import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import locators as loc

class SwitchingBetweenSections:
    
    @pytest.mark.parametrize('button_locator_name, heading_locator_name', [
        ('CONSTRUCTOR_BUNS_BUTTON', 'CONSTRUCTOR_BUNS_HEADING'),
        ('CONSTRUCTOR_SOUSE_BUTTON', 'CONSTRUCTOR_SOUSE_HEADING'),
        ('CONSTRUCTOR_TOPPING_BUTTON', 'CONSTRUCTOR_TOPPING_HEADING')
    ],
    ids=["buns", 
        "sauce", 
        "toppings"
        ])
    def test_switching_between_sections(self, login, button_locator_name, heading_locator_name):
        driver = login

        # Получаем локаторы
        button_locator = getattr(loc, button_locator_name)
        heading_locator = getattr(loc, heading_locator_name)
        
        # Кликаем по кнопке раздела
        driver.find_element(*button_locator).click()
        
        # Проверяем, что заголовок раздела отображается
        target_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(heading_locator)
        )
        assert target_element.is_displayed()