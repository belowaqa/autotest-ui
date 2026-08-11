from playwright.sync_api import sync_playwright, expect

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    login_button_locator = page.get_by_test_id('login-page-login-button')
    expect(login_button_locator).to_be_disabled()

    page.wait_for_timeout(3000)