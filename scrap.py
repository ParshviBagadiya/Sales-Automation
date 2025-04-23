import requests
import pandas as pd

def search_with_serpapi(query, pages=1):
    api_key = "eb31f5ce979985a7add67ea4494a99fcf1fc1b576d279d7563ae453faf3c46b8"
    results = []

    for page in range(pages):
        params = {
            "engine": "google",
            "q": query,
            "hl": "en",
            "gl": "us",
            "start": page * 10,
            "api_key": api_key
        }

        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        for result in data.get("organic_results", []):
            results.append({
                "Company Name": result.get("title"),
                "Website/URL": result.get("link"),
                "Description": result.get("snippet"),
                "Industry": "IT Services",
                "Location": "United States"
            })

    return results

query = "IT services companies in India"
data = search_with_serpapi(query, pages=2)
df = pd.DataFrame(data)
df.to_excel("scraped_icp_companies_india.xlsx", index=False)

print("✅ Done with SerpAPI.")
