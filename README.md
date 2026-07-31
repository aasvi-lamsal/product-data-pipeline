# Product Data Pipeline

An end-to-end data engineering pipeline that extracts product data from an e-commerce website, cleans and transforms the data, stores it in a database, exports datasets, and performs automated data quality checks.

---

## Project Overview

This project demonstrates a complete **ETL (Extract, Transform, Load)** workflow.

The pipeline collects book product information from an online website, processes the raw data into a clean format, stores the processed data, and performs quality validation before generating the final dataset.

This project simulates a real-world data engineering workflow where data is collected, transformed, validated, and stored for further analysis.

---

## Pipeline Architecture

```
                    Website
                       |
                       |
                       ↓
              Web Scraping (Playwright)
                       |
                       |
                       ↓
                Raw Product Data
                       |
                       |
                       ↓
              Data Cleaning (Pandas)
                       |
          ┌────────────┴────────────┐
          ↓                         ↓
     CSV Export              SQLite Database
          |
          |
          ↓
    Data Quality Checks
          |
          |
          ↓
     Validated Dataset
```

---

# Features

- Automated web scraping using Playwright
- Multi-page product extraction
- Data cleaning and transformation using Pandas
- Price conversion from text to numeric format
- Rating conversion from text to numeric values
- Availability standardization
- CSV file generation
- SQLite database storage
- Automated data quality validation
- Complete pipeline execution using one command

---

# Technologies Used

## Programming Language

- Python 3.13

## Libraries

- Playwright
- Pandas
- NumPy

## Database

- SQLite

## Tools

- Virtual Environment (venv)
- Git
- GitHub

---

# Project Structure

```
product-data-pipeline/

│
├── data/
│   ├── products.csv
│   └── products.db
│
├── src/
│   ├── scraper.py
│   ├── cleaner.py
│   ├── database.py
│   ├── exporter.py
│   ├── qa.py
│   └── main.py
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

# How It Works

## 1. Extract

The scraper collects product information from:

```
https://books.toscrape.com
```

Extracted fields:

- Product title
- Price
- Availability
- Rating
- Product URL

The scraper automatically navigates through all pages and collected:

```
1000 books
```

---

## 2. Transform

The cleaning process converts raw scraped data into structured data.

Examples:

Before:

```
Price: £51.77
Rating: star-rating Five
Availability: in stock
```

After:

```
Price: 51.77
Rating: 5
Availability: In Stock
```

---

## 3. Load

The cleaned data is stored in:

### CSV Format

```
data/products.csv
```

### SQLite Database

```
data/products.db
```

Database table:

```
products
```

---

## 4. Data Quality Checks

The pipeline performs automated validation checks:

- Missing values
- Duplicate records
- Invalid prices
- Empty URLs


Example output:

```
========== QA REPORT ==========

Total Records: 1000

Missing Values:
0

Duplicate URLs: 0

Invalid Prices: 0

Empty URLs: 0

===============================
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
```

Navigate to project folder:

```bash
cd product-data-pipeline
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

Run the complete pipeline:

```bash
python src/main.py
```

The pipeline automatically performs:

1. Data extraction
2. Data cleaning
3. CSV export
4. Database creation
5. Data quality validation

---

# Sample Execution Output

```
STARTING DATA PIPELINE

Step 1: Scraping data...

Total books collected: 1000


Step 2: Cleaning data...

Clean records: 1000


Step 3: Exporting CSV...

CSV file created successfully!


Step 4: Creating database...

Database created successfully!


Step 5: Running QA checks...


Total Records: 1000
Duplicate URLs: 0
Invalid Prices: 0
Empty URLs: 0


PIPELINE COMPLETED SUCCESSFULLY!
```

---

# Future Improvements

Future enhancements planned:

- Add PostgreSQL database support
- Add Apache Airflow scheduling
- Add Docker containerization
- Deploy pipeline on AWS
- Add automated logging
- Add monitoring dashboard
- Add cloud data warehouse integration

---

# Skills Demonstrated

This project demonstrates:

- Python programming
- Data extraction
- ETL pipeline development
- Data cleaning
- Data validation
- Database management
- SQL concepts
- Automation
- Project structuring
- Version control with Git

---

# Author

Aasvi Lamsal