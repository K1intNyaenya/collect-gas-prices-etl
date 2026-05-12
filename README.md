# Collect Gas Prices ETL

An Extract-Transform-Load (ETL) pipeline that collects gas price data from the CollectAPI, processes it with Pandas, and loads it into a PostgreSQL database.

## Project Overview

This project automates the collection and processing of gas price data across Washington State. The pipeline:
1. **Extracts** real-time gas price data from the CollectAPI
2. **Transforms** the data into clean, structured formats
3. **Loads** the processed data into PostgreSQL tables

## Features

- Automated gas price data collection from CollectAPI
- Separate extraction of state-level and city-level price data
- Automatic data type conversion and normalization
- PostgreSQL integration with SQLAlchemy ORM
- Clean, modular Python structure

## Prerequisites

- Python 3.10 or higher
- PostgreSQL database
- CollectAPI account with API key
- Required Python packages (see Installation)

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd collect-gas-prices-etl
   ```

2. **Create and activate a virtual environment** (if not already done)
   ```bash
   python3 -m venv gasenv
   source gasenv/bin/activate
   ```

3. **Install required dependencies**
   ```bash
   pip install pandas sqlalchemy psycopg2-binary
   ```

## Setup

### Database Configuration

Update the database connection URL in `load.py`:

```python
av_url = "postgresql+psycopg2://username:password@host:port/database?sslmode=require"
```

### API Configuration

Update the API headers in `extract.py` with your CollectAPI credentials:

```python
headers = {
    'content-type': "application/json",
    'authorization': "apikey YOUR_API_KEY_HERE"
}
```

## Usage

### Run the Complete Pipeline

Execute the load process (which runs all three stages automatically):
```bash
python load.py
```

### Run Individual Stages

**Extract only:**
```bash
python extract.py
```
This fetches gas price data and saves it to `gas_prices.json`.

**Transform only:**
```bash
python transform.py
```
This processes the JSON data and displays state and city statistics.

**Load only:**
```bash
python load.py
```
This transforms the data and loads it into the database.

## Project Structure

```
collect-gas-prices-etl/
├── extract.py           # Fetches gas price data from CollectAPI
├── transform.py         # Cleans and structures the data using Pandas
├── load.py              # Loads data into PostgreSQL database
├── gas_prices.json      # Extracted raw data (generated)
├── README.md            # Project details
└── gasenv/              # Python virtual environment
```

## Technologies Used

- **Python 3.10**: Core programming language
- **Pandas**: Data manipulation and transformation
- **SQLAlchemy**: Database ORM
- **psycopg2**: PostgreSQL adapter
- **CollectAPI**: Real-time gas price data source

## Output

The pipeline creates two tables in PostgreSQL:

- `state_gas_prices`: State-level aggregate gas prices
- `city_gas_prices`: City-level gas prices by type (gasoline, midgrade, premium, diesel)

## Data Types

The following numeric columns are standardized:
- `gasoline`
- `midgrade`
- `premium`
- `diesel`

All column names are converted to lowercase for consistency.

## Notes

```python
import os
api_key = os.getenv('COLLECT_API_KEY')
db_url = os.getenv('DATABASE_URL')
```

## License

This project is part of the data engineering portfolio.

## Author

Created as a data engineering project to practice ETL pipeline development.
