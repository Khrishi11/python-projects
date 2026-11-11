# Project 6: Web Scraping

# The task is to scrape the list of largest companies in US by revenue form wikipedia using 
# Beautiful Soup in Python. The data required to be extracted includes the rank, name of company,
# Industry, Revenue, Revenue growth, Headquaters.

# What is the process to extract data from the wikipedia website using Beautiful Soup in Python?
# Specifically, how can we extract the rank, name of the company, Industry, Revenue, Revenue growth,
# Headquarters for the top US companies by Revenue?

import requests
from bs4 import BeautifulSoup
import pandas as pd


#  the exact Wikipedia page we want to download
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# some websites block requests that don't look like they're coming from a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

# send a GET request to fetch the page, passing our headers along with it
response = requests.get(url, headers=headers)


# --- Check 1: status_code tells us whether the request actually succeeded
print(f"Status code: {response.status_code}\n" if response.status_code == 200 else 
      f'Request failed Status code: {response.status_code}\n') # 200 = OK, anything else means the request failed

# --- Check 2: how many characters of HTML did we download? ---
print(f"Response text length: {len(response.text)}\n") # how many characters of HTML did we download?

# --- Check 3: does the raw HTML contain any <table at all? ---
print(f'Does HTML contain <table>? {"<table" in response.text}\n')

# --- Check 4: try parsing with lxml instead of html.parser ---
soup = BeautifulSoup(response.text, "lxml")
all_tables = soup.find_all("table")
print(f"Number of tables found: {len(all_tables)}\n")

# --- Check 5: look at the first bit of the actual HTML we downloaded ---
print(f"First 2000 characters of HTML:\n{response.text[:2000]}\n")

# --- Check 6: look at the first table's HTML ---
for i, table in enumerate(all_tables):
    headers = table.find_all("th")
    header_text = [h.get_text(strip=True) for h in headers]
    print(f"Table {i}: headers = {header_text}\n")

# --- Check 7: look at the first table's caption ---
main_table = all_tables[0]
caption = main_table.find("caption")
print(f"Main table caption: {caption.get_text(strip=True) if caption else 'No caption found'}\n")



# --- Check 8: look at the number of rows in the main table ---
rows = main_table.find_all("tr")
print(f"Number of rows in main table: {len(rows)}\n")

company_data = []  # will hold one dictionary per company

# skip the first row (index 0), since that's the header row, not real data
for row in rows[1:]:
    cells = row.find_all("td")

    # pull just the visible text out of each cell, stripping extra whitespace
    values = [cell.get_text(strip=True) for cell in cells]
    
        # build a dictionary for this company, matching each value to its column name
    company = {
        "Rank": values[0],
        "Name": values[1],
        "Industry": values[2],
        "Revenue (USD millions)": values[3],
        "Revenue growth": values[4],
        "Employees": values[5],
        "Headquarters": values[6]
    }
    
    company_data.append(company)

print(f"First company: {company_data[0]}\n")   # check the first entry looks right
print(f"Total companies: {len(company_data)}\n") # should be 100

# Create a DataFrame from the list of dictionaries and save it to a CSV file
df = pd.DataFrame(company_data)

print(f"First 5 rows:\n {df.head()}\n")  # peek at the first 5 rows to sanity check

# Save the DataFrame to a CSV file
df.to_csv("largest_us_companies_by_revenue.csv", index=False)
print(f"Saved to CSV: {df.shape[0]} rows and {df.shape[1]} columns")