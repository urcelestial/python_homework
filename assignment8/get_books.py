from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

import json
import pandas as pd

# TASK 3

# Load the web page given in task 2
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

# Find all the li elements in the page from the search list results
li_elements = driver.find_elements(By.CSS_SELECTOR,'li')


# Main loop (iterating through the li entries)
results = []
if (li_elements):
    # Find the title of each book and get the text for that entry
    for li in li_elements:
        title_element = li.find_element(By.CSS_SELECTOR, 'h3 a')
        if title_element:
            # Find the authors of each book and get the text for each entry
            author_elements = li.find_elements(By.CSS_SELECTOR, '.cp-author a')
            if author_elements:
                # Find the div that contains the format and the year
                format_year_element = li.find_element(By.CSS_SELECTOR, '.cp-format-year')
                if format_year_element:
                    # Find the span entry within it that contains this information
                    span_element = format_year_element.find_element(By.CSS_SELECTOR, 'span')

            book_dict = {
                "Title": title_element.text,
                "Author": "; ".join([author.text for author in author_elements]) if author_elements else "",
                "Format-Year": format_year_element.text if format_year_element else ""
            }
            results.append(book_dict)

# Convert the results to a DataFrame and save as JSON and CSV
df = pd.DataFrame(results)
print(df)

df.to_csv("get_books.csv", index=False)
df.to_json("get_books.json", orient="records", indent=4)
