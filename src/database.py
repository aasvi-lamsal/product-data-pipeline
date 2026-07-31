import sqlite3
import pandas as pd


def create_database(df):
    """
    Saves cleaned product data into SQLite database.
    """

    database_path = "data/products.db"

    # Connect to SQLite database
    connection = sqlite3.connect(database_path)

    # Save dataframe into database table
    df.to_sql(
        "products",
        connection,
        if_exists="replace",
        index=False
    )

    # Close connection
    connection.close()

    print("Database created successfully!")
    print("Saved table: products")


if __name__ == "__main__":

    sample_data = {
        "title": ["Test Book"],
        "price": [20.5],
        "availability": ["In Stock"],
        "rating": [5],
        "url": ["https://example.com"]
    }

    df = pd.DataFrame(sample_data)

    create_database(df)