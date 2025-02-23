PERSONAL_ACCOUNT_LOCATOR = ".//a[@href='/account']" #  Локатор кнопки "Личный кабинет"
REGISTRATION_BUTTON_LOCATOR = ".//a[@href='/register']" #  Локатор кнопки "Зарегистрироваться" на странице Личного кабинета
REGISTRATION_FORM_TITLE_LOCATOR = ".//h2[contains(text(),'Регистрация')]" #  Локатор заголовка формы регистрации "Регистрация"
REGISTRATION_NAME_INPUT_LOCATOR = ".//label[contains(text(),'Имя')]/following-sibling::input" #  Поле ввода имени нового пользователя
REGISTRATION_EMAIL_INPUT_LOCATOR = ".//label[contains(text(),'Email')]/following-sibling::input" #  Поле ввода Емэйла нового пользователя
REGISTRATION_PASSWORD_INPUT_LOCATOR = ".//label[contains(text(),'Пароль')]/following-sibling::input" #  Поле ввода пароля нового пользователя
COMPLETE_REGISTRATION_BUTTON = ".//button[contains(text(),'Зарегистрироваться')]" #  Кнопка завершения регистрации на Форме регистрации
ERROR_TEXT_INPUT_LOCATOR = ".//p[contains(@class,'input__error')]" #  Текст с ошибкой "Некорректный пароль"
AUTH_EMAIL_INPUT_LOCATOR = ".//input[@name='name']" #  Поле ввода Емэйла существующего пользователя
AUTH_PASSWORD_INPUT_LOCATOR = ".//input[@name='Пароль']" #  Поле ввода Пароля существующего пользователя
AUTH_FORM_TITLE_LOCATOR = ".//h2[text()='Вход']" #  Локатор заголовка формы авторизации "Вход"
AUTH_BUTTON_LOCATOR = ".//button[text()='Войти']" #  Локатор кнопки "Войти" на форме авторизации
GO_TO_AUTH_BUTTON_LOCATOR = ".//button[text()='Войти в аккаунт']" #  Локатор кнопки перехода к авторизации "Войти в аккаунт" на главной странице
GO_TO_AUTH_FORM_BUTTON_LOCATOR = ".//a[@href='/login']" #  Локатор кнопки "Войти" на странице регистрации нового пользователя
FORGOT_PASSWORD_BUTTON_LOCATOR = ".//p[contains(text(),'Забыли пароль?')]" #  Локатор кнопки "Восстановить пароль" на странице авторизации пользователя
FORGOT_PASSWORD_PAGE_TITLE_LOCATOR = ".//h2[text()='Восстановление пароля']" #  Локатор заголовка формы восстановления пароля "Восстановление пароля"
LOGOUT_BUTTON_LOCATOR = ".//button[contains(text(), 'Выход')]" #  Локатор кнопки "Выход" в Личном кабинете
LOGO_LOCATOR = ".//div[@class='AppHeader_header__logo__2D0X2']/a" #  Локатор логотипа сайта
MAIN_MENU_TITLE_LOCATOR = ".//h1[contains(text(), 'Соберите бургер')]" #  Локатор заголовка "Соберите бургер" Главной страницы
CONSTRUCTOR_BUTTON_LOCATOR = ".//p[text() = 'Конструктор']" #  Локатор кнопки "Конструктор" на Главной странице
ROLLS_CHAPTER_LOCATOR = ".//span[text()='Булки']/.." #  Локатор раздела "Булки" на Главной странице
INDICATION_SELECT_LOCATOR = "//div[contains(@class, 'tab_tab_type_current')]/span" # Локатор индикатора подсветки выбранного раздела
SAUCES_CHAPTER_LOCATOR = ".//span[text()='Соусы']/.." # Локатор раздела "Соусы" на Главной странице
FILLINGS_CHAPTER_LOCATOR = ".//span[text()='Начинки']/.." #Локатор раздела "Начинки" на Главной странице