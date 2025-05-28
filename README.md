# News Scraper for NV.ua

This project is a simple web scraper built with Python that collects news headlines from [nv.ua](https://nv.ua/ukr/ukraine.html) (Ukrainian news website). It scrapes article titles, links, and publication dates, and saves the data into both CSV and JSON formats.

## Features

- Collects news data from multiple pages

- Parses article title, link, and publication date

- Saves results to:
  - `news.csv` – for tabular data
  - `news.json` – for structured JSON output

- Uses randomized delay between requests to avoid overloading the server

## Technologies Used

- Python 3

- [cloudscraper](https://pypi.org/project/cloudscraper/) – to bypass Cloudflare protection

- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/) – for HTML parsing

- [lxml](https://pypi.org/project/lxml/) – HTML/XML parser

- Built-in `csv`, `json`, `time`, and `random` modules

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/UaBogdan2004/nv_ua.git
   cd nv_ua
   
2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install the required packages:
    ```bash
   pip install -r requirements.txt

## Usage
1. Run the scraper with:
    ```bash
    python main.py

The script will start scraping news from the first 99 pages of https://nv.ua/ukr/ukraine.html and save the output to:

- news.csv

- news.json

## Notes
This project is for educational and portfolio purposes.

Please respect the website’s robots.txt and terms of service.