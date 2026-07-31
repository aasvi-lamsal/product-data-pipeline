from playwright.sync_api import sync_playwright
import os


def take_website_screenshot():

    os.makedirs("screenshots", exist_ok=True)

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            viewport={"width": 1400, "height": 900}
        )

        page.goto("https://books.toscrape.com")

        page.screenshot(
            path="screenshots/website.png",
            full_page=True
        )

        browser.close()

        print("Website screenshot saved!")


if __name__ == "__main__":
    take_website_screenshot()