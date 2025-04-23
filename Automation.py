import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.parse
import time

def google_search_scraper(query, num_pages=1):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    results = []

    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}&start={start}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        print(soup.prettify())

        for result in soup.find_all("div", class_="g"):
            title = result.find("h3")
            link = result.find("a", href=True)
            snippet = result.find("span")  # or find("div") with class check
            if title and link:
                results.append({
                    "Company Name": title.get_text(),
                    "Website/URL": link["href"],
                    "Description": snippet.get_text() if snippet else "",
                    "Industry": "IT Services",
                    "Location": "United States"
                })


        time.sleep(1)  # Be nice to Google :)

    return results

# Define ICP-based query
query = "IT services companies in United States"

# Get results
scraped_data = google_search_scraper(query, num_pages=2)

# Store in DataFrame
df = pd.DataFrame(scraped_data)

# Save to Excel
df.to_excel("scraped_icp_companies.xlsx", index=False)

print("✅ Data scraping complete. Results saved to 'scraped_icp_companies.xlsx'.")
