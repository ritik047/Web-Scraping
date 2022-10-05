"""
REPO: https://github.com/ritik047/Web-Scraping
DATE: 2022-10-03
USAGE: Python script for getting the top Linux distros in the last 30 days.
It queries https://distrowatch.com/dwres.php?resource=popularity to get the data.
"""

# Define imports
from bs4 import BeautifulSoup
import requests


# Get the data
r = requests.get("https://distrowatch.com/dwres.php?resource=popularity", timeout=10)
soup = BeautifulSoup(r.content, 'html.parser')
vals = soup.find_all('td', class_="phr2")

# As BeautifulSoup will return all the distros from all categories,
# we need to select the last 264 values in the last column
last_12_months = vals[792:1056]

# Print out the data, in order, with it's ranking and name.
for c,v in enumerate(last_12_months):
    print(f"{c+1}: {v.text}")
