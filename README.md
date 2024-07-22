# Phone Number Extractor

## Overview

**Phone Number Extractor** is a Python-based project designed to extract phone numbers from text data. It supports various phone number formats, including numeric digits, words representing numbers, and special Unicode characters. This project is ideal for applications such as customer service, data cleaning, web scraping, and more.

## Features

- Extracts phone numbers from text in various formats:
  - Numeric digits (e.g., `123-456-7890`)
  - Words representing numbers (e.g., `one two three four five six seven eight nine zero`)
  - Special Unicode characters
- Handles different phone number formats, including:
  - `(123) 456-7890`
  - `123-456-7890`
  - `123 456 7890`
  - `1234567890`
- Validates and cleans extracted phone numbers.

## Project Structure

- `scraper.py`: Contains the core logic for extracting phone numbers.
- `data.py`: Provides test data for verifying the phone number extraction functionality.
- `test_scraper.py`: Contains the test cases to validate the extraction logic.

## Dependencies

- `pandas` (optional, for data manipulation in practical use cases)
- `re` (for regular expressions)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Deathbringer98/phone-number-extractor.git
   cd phone-number-extractor
## Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the required dependencies:
pip install pandas

## Usage
Extracting Phone Numbers
Use the get_all_nums function from scraper.py to extract phone numbers from a given text:
```
import scraper

text = "Call me at 123-456-7890 or (123) 456-7890."
phone_numbers = scraper.get_all_nums(text)
print(phone_numbers)  # Output: ['1234567890', '1234567890']
```

## Running Tests
To run the tests and validate the functionality, execute the test_scraper.py script:

python test_scraper.py

## Example Code
Extracting Phone Numbers from Customer Emails

```
import scraper

def extract_numbers_from_emails(email_texts):
    phone_numbers = []
    for email in email_texts:
        phone_numbers.extend(scraper.get_all_nums(email))
    return phone_numbers

# Example email texts
emails = [
    "Hello, you can reach me at 123-456-7890 or 9876543210.",
    "My new number is (123) 456-7890. Call me!"
]

phone_numbers = extract_numbers_from_emails(emails)
print(phone_numbers)  # ['1234567890', '9876543210', '1234567890']

```

## Data Cleaning in a CSV File
```
import pandas as pd
import scraper

# Load the CSV file
df = pd.read_csv('contacts.csv')

# Function to extract phone numbers from a dataframe column
def extract_phone_numbers(df, column_name):
    df['cleaned_phone_numbers'] = df[column_name].apply(lambda x: scraper.get_all_nums(x))
    return df

# Apply the function to the relevant column
df = extract_phone_numbers(df, 'phone_field')

# Save the cleaned dataframe to a new CSV file
df.to_csv('cleaned_contacts.csv', index=False)
```







