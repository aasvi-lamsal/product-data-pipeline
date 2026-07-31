from scraper import scrape_all_books
from cleaner import clean_data
from database import create_database
from exporter import save_to_csv
from qa import run_quality_checks, print_report


def main():
    """
    Runs the complete data pipeline.
    """

    print("\nSTARTING DATA PIPELINE\n")

    # 1. Extract data
    print("Step 1: Scraping data...")
    books = scrape_all_books()

    print(f"Total books collected: {len(books)}")


    # 2. Transform data
    print("\nStep 2: Cleaning data...")
    cleaned_df = clean_data(books)

    print(f"Clean records: {len(cleaned_df)}")


    # 3. Save CSV
    print("\nStep 3: Exporting CSV...")
    save_to_csv(cleaned_df)


    # 4. Save Database
    print("\nStep 4: Creating database...")
    create_database(cleaned_df)


    # 5. Run QA checks
    print("\nStep 5: Running QA checks...")
    report = run_quality_checks(cleaned_df)

    print_report(report)


    print("\nPIPELINE COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    main()