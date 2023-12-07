# Stock Data Scraper

This script is designed to scrape and update stock market data from two sources: Market Watch and the Trinidad and Tobago Stock Exchange (TTSE). It also collects exchange rates from the Central Bank of Trinidad and Tobago (CBTT). The scraped data is then stored in a SQLite database for further analysis.

## Requirements
- Python 3.x
- Required Python packages: `js2py`, `requests`, `beautifulsoup4`, `pandas`, and `sqlalchemy`

## Setup
1. Install the required Python packages using the following command:
`pip install js2py requests beautifulsoup4 pandas sqlalchemy`
2. Ensure you have a working SQLite database for storing the scraped data.

## Usage
1. Update the `HEADER` variable with the desired User-Agent string.
2. Set the database location by updating the `Location` variable.
3. Run the script to scrape and update stock market data.

## Database Schema
The script uses an SQLite database with the following schema:

### Table: stock_data
- `id` (Primary Key)
- `stock_Name` (Stock name)
- `stock_Code` (Stock code)
- `OPEN` (Opening stock price)
- `CLOSE` (Closing stock price)
- `VOLUME_TRADED` (Volume traded)
- `stock_date` (Date of the stock data)

### Table: cbtt_rates
- `id` (Primary Key)
- `Canadian_Buy` (Buying rate for Canadian dollars)
- `Canadian_Sell` (Selling rate for Canadian dollars)
- `US_Buy` (Buying rate for US dollars)
- `US_Sell` (Selling rate for US dollars)
- `CBDate` (Date of the exchange rates)

## Functions
The script contains several functions:

1. `getCBTTRATES()`: Scrapes exchange rates from CBTT and returns a DataFrame.
2. `add_to_db(session, df, codeName, code)`: Adds stock data to the database.
3. `add_to_db_CBTT(session, df)`: Adds CBTT exchange rates to the database.
4. `get_variable(encoded_script)`: Decodes and extracts a variable from encoded JavaScript.

## Update Log
- **Last Updated**: 2023-11-07
- New Sucuri Website Firewall Blockage broke code previously. Fixed

## Notes
- The script updates stock data for predefined stock codes from Market Watch and TTSE.
- Exchange rates from CBTT are scraped separately.
- The script uses SQLAlchemy for database operations.

## Disclaimer
This script is for educational purposes only. Use it responsibly and ensure compliance with the terms of use of the targeted websites.

