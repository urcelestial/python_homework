import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(10)

# Starting Point
driver.get("https://owasp.org/www-project-top-ten/")

scrapped_links = []

# Extract the top ten from the 2025 link
link_elements = driver.find_elements(By.XPATH, '//section[contains(@class, "page-body")]//a')

for link in link_elements:
    Title = link.text.strip()
    Url = link.get_attribute("href")
    
    # Capitalized keys: "Title" and "URL"
    if Title and Url:
        scrapped_links.append({"Title": Title, "Url": Url})

driver.quit()

print(scrapped_links)

# Export to CSV with capitalized headers ("Title", "URL") inside assignment8 folder
df = pd.DataFrame(scrapped_links)
df.to_csv("assignment8/owasp_top_10.csv", index=False)