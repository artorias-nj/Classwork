import urllib.request, urllib.error
from bs4 import BeautifulSoup
import ssl
from collections import Counter
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_films'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Find the correct wikitable (the first one is correct here)
table = soup.find('table', {'class': 'wikitable'})

total_gross = 0
years = []

for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) >= 5:
        # Safely get gross and clean it
        gross_text = cols[3].get_text(separator=" ", strip=True)
        gross_text = re.sub(r'[^0-9]', '', gross_text)
        if gross_text:
            total_gross += int(gross_text)
        
        # Safely get year
        year_text = cols[4].get_text(strip=True)
        # Ensure it's just a year (4 digits)
        year_match = re.search(r'\b(19|20)\d{2}\b', year_text)
        if year_match:
            years.append(year_match.group(0))

# Calculate the most common year
year_counter = Counter(years)
most_common_year, count = year_counter.most_common(1)[0]

# Display results
print(f"\nTotal Worldwide Gross: ${total_gross:,.0f}")
print(f"Most common year: {most_common_year} (appears {count} times)")
