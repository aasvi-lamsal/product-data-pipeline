from playwright.sync_api import sync_playwright
from urllib.parse import urljoin


def scrape_page(page):
    """
    Scrape all books from the current page.
    Returns a list of dictionaries.
    """

    books = []

    book_cards = page.locator("article.product_pod")
    count = book_cards.count()

    print(f"Found {count} books on this page.")

    for i in range(count):
        book = book_cards.nth(i)

        title = book.locator("h3 a").get_attribute("title")
        price = book.locator("p.price_color").text_content().strip()
        availability = (
            book.locator("p.instock.availability")
            .text_content()
            .strip()
        )

        rating = book.locator("p.star-rating").get_attribute("class")

        relative_url = book.locator("h3 a").get_attribute("href")
        product_url = urljoin(page.url, relative_url)

        books.append(
            {
                "title": title,
                "price": price,
                "availability": availability,
                "rating": rating,
                "url": product_url,
            }
        )

    return books


def scrape_all_books():
    """
    Scrape every page of the website.
    """

    all_books = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://books.toscrape.com")

        page_number = 1

        while True:

            print(f"\nScraping Page {page_number}")

            books = scrape_page(page)
            all_books.extend(books)

            next_button = page.locator("li.next a")

            if next_button.count() == 0:
                print("\nReached the last page.")
                break

            next_button.click()
            page.wait_for_load_state("networkidle")

            page_number += 1

        browser.close()

    return all_books


if __name__ == "__main__":

    books = scrape_all_books()

    print(f"\nTotal books scraped: {len(books)}")