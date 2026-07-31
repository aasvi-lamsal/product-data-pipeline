import pandas as pd


def run_quality_checks(df):
    """
    Performs data quality checks on cleaned product data.
    """

    report = {}

    # Total number of records
    report["Total Records"] = len(df)

    # Check missing values
    report["Missing Values"] = df.isnull().sum().to_dict()

    # Check duplicate products
    report["Duplicate URLs"] = df["url"].duplicated().sum()

    # Check invalid prices
    report["Invalid Prices"] = (
        (df["price"] <= 0).sum()
    )

    # Check empty URLs
    report["Empty URLs"] = (
        df["url"]
        .isnull()
        .sum()
    )

    return report


def print_report(report):
    """
    Prints QA report in readable format.
    """

    print("\n========== QA REPORT ==========\n")

    for key, value in report.items():
        print(f"{key}: {value}")

    print("\n===============================")


if __name__ == "__main__":

    sample_data = {
        "title": [
            "Test Book",
            "Another Book"
        ],
        "price": [
            20.5,
            30.0
        ],
        "availability": [
            "In Stock",
            "In Stock"
        ],
        "rating": [
            5,
            4
        ],
        "url": [
            "https://example.com",
            "https://example.com/book2"
        ]
    }


    df = pd.DataFrame(sample_data)

    report = run_quality_checks(df)

    print_report(report)