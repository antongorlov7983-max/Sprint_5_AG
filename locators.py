from selenium.webdriver.common.by import By


# Форма регистрации
REGISTRATION_NAME_INPUT = (By.XPATH,'.//label[contains(text(),"Имя")]/parent::div/input') #  Поле "Имя"
REGISTRATION_EMAIL_INPUT = (By.XPATH,'.//label[contains(text(),"Email")]/parent::div/input') # поле "Email" 
REGISTRATION_PASSWORD = (By.XPATH,'.//label[contains(text(),"Пароль")]/parent::div/input') # Поле "Пароль" 
REGISTRATION_BUTTON = (By.XPATH,'.//button[contains(text(),"Зарегистрироваться")]') # Кнопка "Зарегистрироваться"
REGISTRATION_LOGIN_BUTTON = (By.XPATH,'.//a[contains(text(),"Войти")]') # Кнопка "Войти" на форму авторизации

REGISTRATION_PASSWORD_ERROR = (By.CSS_SELECTOR,'.input__error') # Встплывающее сообщение об ошибке "Некорректный пароль" - Для проверки, при не валидном пароле при регистрации

# Форма авторизации
LOGIN_EMAIL_INPUT= (By.XPATH,'.//input[@name="name"]') # Поле "Email"
LOGIN_PASSWORD_INPUT = (By.XPATH,'.//input[@name="Пароль"]') # Поле "Пароль"
LOGIN_BUTTON = (By.XPATH,'.//button[contains(text(),"Войти")]') # Кнопка "Войти"

# Главная страница 
MAIN_PAGE_LOGIN_ACCOUNT_BUTTON = (By.XPATH,'.//button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт"(не авторизирован) на форму авторизации
MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON = (By.XPATH,'.//p[text()="Личный Кабинет"]') # Кнопка "Личный Кабинет" 

ORDER_BUTTON = (By.XPATH,'.//button[contains(text(),"Оформить заказ")]') # Кнопка "Оформить заказ" - Для проверки авторизации

# Форма восcтановления пароля
PASSWORD_RECOVERY_LOGIN_BUTTON = (By.XPATH,'.//a[contains(text(),"Войти")]') # Кнопка "Войти"  на форму авторизации

# Страница личного кабинета
PA_LOGO = (By.CLASS_NAME,'AppHeader_header__logo__2D0X2') # Логотип приложения 
PA_DESIGNER_BUTTON = (By.XPATH,'.//p[contains(text(),"Конструктор")]/parent::a') # Кнопка "Конструктор"
LOGOUT_BUTTON = (By.XPATH,'//button[contains(text(),"Выход")]') # Кнопка "Выход"

# Страница конструктора
CONSTRUCTOR_MENU_INGREDIENTS =(By.CLASS_NAME,'BurgerIngredients_ingredients__menuContainer__Xu3Mo')
CONSTRUCTOR_BUNS_BUTTON = (By.XPATH,'.//span[contains(text(),"Булки")]/parent::div') # Кнопка перехода в раздел "Булки"
CONSTRUCTOR_SOUSE_BUTTON = (By.XPATH,'.//span[contains(text(),"Соусы")]/parent::div') # Кнопка перехода в раздел "Соусы"
CONSTRUCTOR_TOPPING_BUTTON = (By.XPATH,'.//span[contains(text(),"Начинки")]/parent::div') # Кнопка перехода в раздел "Начинки"


CONSTRUCTOR_BUNS_HEADING = (By.XPATH,'.//h2[contains(text(),"Булки")]') # Заголовок раздела "Булки" - Для проверки работы кнопки "Булки"
CONSTRUCTOR_SOUSE_HEADING = (By.XPATH,'.//h2[contains(.,"Соусы")]') # Заголовок раздела "Соусы" - Для проверки работы кнопки "Соусы"
CONSTRUCTOR_TOPPING_HEADING = (By.XPATH,'.//h2[contains(.,"Начинки")]') # Заголовок раздела "Начинки" - Для проверки работы кнопки "Начинки"


