from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input_locator = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input_locator.fill('user.name@gmail.com')

    username_input_locator = page.get_by_test_id('registration-form-email-input').locator('input')
    username_input_locator.fill('username')

    password_input_locator = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input_locator.fill('password')

    button_locator = page.get_by_test_id('registration-page-registration-button')
    button_locator.click()

    title_locator = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(title_locator).to_be_visible()
    expect(title_locator).to_have_text('Dashboard')
    page.wait_for_timeout(5000)