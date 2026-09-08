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

# Starting page
driver.get("https://owasp.org/www-project-top-ten/")

# Extract the URL for the OWASP Top Ten 2025 page
top_2025_link = driver.find_element(By.XPATH, '//a[contains(@href, "/Top10/2025/")]')
target_url = top_2025_link.get_attribute("href")

# Directing to the 2025 page
driver.get(target_url)

scrapped_links = []

# Extract all vulnerability items from the ordered list 
link_elements = driver.find_elements(By.XPATH, '//ol/li/a')

for link in link_elements:
    Title = link.text.strip()
    Url = link.get_attribute("href")
    if Title and Url:
        scrapped_links.append({"Title": Title, "Url": Url})

driver.quit()

#Print and export to CSV
print(scrapped_links)

df = pd.DataFrame(scrapped_links)
df.to_csv("assignment8/owasp_top_10.csv", index=False)