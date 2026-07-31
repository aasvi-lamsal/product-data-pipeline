import pandas as pd


def save_to_csv(df):
    """
    Saves cleaned product data to CSV file.
    """

    file_path = "data/products.csv"

    df.to_csv(
        file_path,
        index=False
    )

    print("CSV file created successfully!")
    print(f"Saved location: {file_path}")


if __name__ == "__main__":

    sample_data = {
        "title": ["Test Book"],
        "price": [20.5],
        "availability": ["In Stock"],
        "rating": [5],
        "url": ["https://example.com"]
    }

    df = pd.DataFrame(sample_data)

    save_to_csv(df)