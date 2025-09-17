import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os 

driver = uc.Chrome()
driver.maximize_window()
driver.get("https://google.com")
time.sleep(1)

search_box = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
time.sleep(1)
import random
import time

for char in "song lyrics finder":
    search_box.send_keys(char)
    time.sleep(random.uniform(0.2, 0.1))  
search_box.send_keys(Keys.RETURN)
time.sleep(1)

first_data = driver.find_element(By.XPATH , '//*[@id="rso"]/div[1]/div/div/div/div[1]/div/div/span/a/h3')
first_data.click()
time.sleep(1)

search_item = driver.find_element(By.XPATH,'//*[@id="search-word"]')
search_item.send_keys("kabhi kabhi")
search_item.send_keys(Keys.RETURN)
time.sleep(5)

results = driver.find_elements(By.CSS_SELECTOR,'.gsc-webResult.gsc-result')

songs = []
for r in results:
    try:
        title = r.find_element(By.CSS_SELECTOR, ".song-title").text
        link = r.find_element(By.CSS_SELECTOR, "a.gs-title").get_attribute("href")
        if title and link:
            songs.append({"title": title, "link": link})
    except:
        pass
excel_file_path = "kabhi_kabhi_results.xlsx"
# Save results to Excel
if os.path.exists(excel_file_path):
    os.remove(excel_file_path)
    
if songs:
    df = pd.DataFrame(songs)
    df.to_excel(excel_file_path, index=False)
    print(" Saved results to kabhi_kabhi_results.xlsx")
else:
    print(" No results found — maybe the site’s structure is different.")



# breakpoint()
driver.quit()