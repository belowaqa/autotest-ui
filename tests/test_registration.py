import os
import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()


        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill('user@gmail.com')

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill('username')

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill('password')

        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        os.makedirs('cookie', exist_ok=True)  # Гарантирует наличие папки cookie
        context.storage_state(path='cookie/browser-state.json')

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context(storage_state='cookie/browser-state.json')
        page = context.new_page()

        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')


    if os.path.exists('cookie/browser-state.json'):
        os.remove('cookie/browser-state.json')
