from playwright.sync_api import sync_playwright

print("Тест запускается...")

expected_title = "Fast and reliable end-to-end testing for modern web apps | Playwright"
browsers = ["chromium", "firefox"]

def check_page_title():
    with sync_playwright() as playwright:
        for browser_name in browsers:
            browser = getattr(playwright, browser_name).launch()
            page = browser.new_page()
            page.goto("https://playwright.dev/")
            # Получаем заголовок напрямую из тега <title> в DOM
            title = page.eval_on_selector("title", "el => el.textContent")
            print(f"[{browser_name}] Заголовок из DOM: '{title}'")
            assert title == expected_title, f"[{browser_name}] Expected '{expected_title}', but got '{title}'"
            print(f"[{browser_name}] Проверка заголовка прошла успешно.")
            browser.close()

check_page_title()