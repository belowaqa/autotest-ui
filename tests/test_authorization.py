from playwright.sync_api import sync_playwright, expect

def test_wrong_email_or_password_authorization():

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

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