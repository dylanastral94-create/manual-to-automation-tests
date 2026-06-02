# Test 1: Demo login page validation
# This test opens a demo site and checks login works

from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        assert "inventory.html" in page.url
        print("Test passed: Login successful!")
        browser.close()

test_login()
