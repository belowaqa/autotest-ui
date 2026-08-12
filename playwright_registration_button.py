from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless = False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email = 'user.name@gmail.com'
    username = 'username'
    password = 'password'

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()
    print('Кнопка недоступна')

    email_locator = page.get_by_test_id('registration-form-email-input').locator('input')
    email_locator.fill(email)

    username_locator = page.get_by_test_id('registration-form-username-input').locator('input')
    username_locator.fill(username)

    password_locator = page.get_by_test_id('registration-form-password-input').locator('input')
    password_locator.fill(password)

    expect(registration_button).to_be_enabled()
    print('Кнопка доступна')

    page.wait_for_timeout(3000)
