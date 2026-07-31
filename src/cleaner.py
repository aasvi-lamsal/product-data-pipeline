import pandas as pd


def convert_rating(rating):
    """
    Converts rating text into numeric value (1-5).
    """

    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    rating_word = rating.split()[-1]

    return rating_map.get(rating_word)


def clean_data(books):
    """
    Cleans scraped book data and returns a cleaned DataFrame.
    """

    # Convert scraped data into DataFrame
    df = pd.DataFrame(books)

    # Remove currency symbol and convert price to float
    df["price"] = (
        df["price"]
        .str.replace("£", "", regex=False)
        .astype(float)
    )

    # Standardize availability text
    df["availability"] = (
        df["availability"]
        .str.strip()
        .str.title()
    )

    # Convert rating text into numbers
    df["rating"] = df["rating"].apply(convert_rating)

    # Remove duplicate products using URL
    df = df.drop_duplicates(subset="url")

    # Remove rows with missing important values
    df = df.dropna(
        subset=[
            "title",
            "price",
            "availability",
            "rating",
            "url"
        ]
    )

    return df


if __name__ == "__main__":

    from scraper import scrape_all_books

    # Extract data from website
    books = scrape_all_books()

    print(f"Raw books collected: {len(books)}")

    # Clean scraped data
    cleaned_df = clean_data(books)

    print("\nCleaned Data:")
    print(cleaned_df.head())