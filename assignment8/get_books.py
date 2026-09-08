import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.implicitly_wait(10)

driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

# Find all search result items
li_elements = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')

results = []

for li in li_elements:
    try:
        # Extract title
        title_element = li.find_element(By.CSS_SELECTOR, 'h3 span.title-content')
        title = title_element.text.strip() if title_element else ""

        # Extract authors
        author_elements = li.find_elements(By.CSS_SELECTOR, 'a.author-link')
        authors = "; ".join([author.text.strip() for author in author_elements]) if author_elements else ""

        # Extract format and year
        format_year_elements = li.find_elements(By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary')
        format_year = format_year_elements[0].text.strip() if format_year_elements else ""

        if title:
            results.append({
                "Title": title,
                "Author": authors,
                "Format-Year": format_year
            })
    except Exception as e:
        continue

driver.quit()

# Convert results to DataFrame and export
df = pd.DataFrame(results)
print(df)

df.to_csv("assignment8/get_books.csv", index=False)
df.to_json("assignment8/get_books.json", orient="records", indent=4)