# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# from dump_excel import dump_to_excel   # import your function

# # Setup Chrome
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# # Open Flipkart
# driver.get("https://www.flipkart.com")
# time.sleep(2)

# # Close login popup
# try:
#     driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
# except:
#     pass

# # Search for phones
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("phones")
# search_box.send_keys(Keys.RETURN)
# time.sleep(3)

# # Scrape phone data
# phone_data = []
# product_cards = driver.find_elements(By.XPATH, "//div[@class='tUxRFH']")

# for card in product_cards:
#     try:
#         name = card.find_element(By.XPATH, ".//div[@class='KzDlHZ']").text
#     except:
#         name = "N/A"

#     try:
#         price = card.find_element(By.XPATH, ".//div[contains(@class,'Nx9bqj')]").text
#     except:
#         price = "N/A"

#     try:
#         specs = card.find_element(By.XPATH, ".//ul[@class='G4BRas']").text
#     except:
#         specs = "N/A"

#     if name != "N/A" and price != "N/A":
#         phone_data.append({"name": name, "price": price, "specs": specs})

# # Dump results into Excel
# dump_to_excel(phone_data, "flipkart_phones.xlsx")

# driver.quit()

def scrape_flipkart(query="phones"):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    from dump_excel import dump_to_excel

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    driver.get("https://www.flipkart.com")
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
    except:
        pass

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    phone_data = []
    product_cards = driver.find_elements(By.XPATH, "//div[@class='tUxRFH']")

    for card in product_cards:
        try:
            name = card.find_element(By.XPATH, ".//div[@class='KzDlHZ']").text
        except:
            name = "N/A"

        try:
            price = card.find_element(By.XPATH, ".//div[contains(@class,'Nx9bqj')]").text
        except:
            price = "N/A"

        try:
            specs = card.find_element(By.XPATH, ".//ul[@class='G4BRas']").text
        except:
            specs = "N/A"

        if name != "N/A" and price != "N/A":
            phone_data.append({"name": name, "price": price, "specs": specs})

    driver.quit()
    return phone_data
