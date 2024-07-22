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


