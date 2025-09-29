from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()


class WebTesting:
    def __init__(self, url, driver=driver):
        self.url = url
        self.driver = driver
        time.sleep(1)

    def search_by_text(self, text):
        self.driver.get(self.url)
        time.sleep(2)
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        first_result = self.driver.find_element(By.ID, "video-title").text
        time.sleep(1)
        return first_result
    
    
tester = WebTesting("https://www.youtube.com")
result = tester.search_by_text("Yellowstone TV Show")
print("Search Result (First):", result)



    
    
    
        # time.sleep(1)
        
# driver.get("https://www.youtube.com")

# time.sleep(1)

# search_box = driver.find_element(By.NAME, "search_query")
# search_box.send_keys("Yellowstone TV Show")
# search_button = driver.find_element(By.ID, "search-icon-legacy")
# search_button.click()
# # search_box.send_keys(Keys.RETURN)
# time.sleep(2)

# first_result = driver.find_element(By.ID, "video-title").text
# print("Search Result (First):", first_result)
# time.sleep(15)


