from playwright.sync_api import sync_playwright, expect

# with отвечает за автоматический запуск (инициализирует и запускает сессию pw)
# завершающие действия (закрывает фоновые процессы, освобождает оперативку)
# sync_playwright() - инциализирует и подготавливает движок pw к работе.
# Синхронный режим - код выполняется строчка за строчкой
# as - записывает результат работы в переменную через которую получаем доступ ко всем возможностям библиотеки

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    # открываем новую страницу для работы. pw может работать с несколькими страницами
    page = browser.new_page()
    # Открытие страницы
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Поиск локаторов и назначение в переменную
    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    password_input = page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill('password')

    login_button = page.get_by_test_id('login-page-login-button')
    login_button.click()

    error_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
    # проверка видимости элемента и нужного текста
    expect(error_alert).to_be_visible()
    expect(error_alert).to_have_text("Wrong email or password")

    page.wait_for_timeout(5000)