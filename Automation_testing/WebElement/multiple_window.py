from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1. Login
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(5)

parent_window_id = driver.current_window_handle
print(parent_window_id)

driver.find_element(By.LINK_TEXT, "Click Here").click()

all_window_ids = driver.window_handles
print(all_window_ids)

for child_window_id in all_window_ids:
    if child_window_id not in parent_window_id:
        driver.switch_to.window(child_window_id)
        driver.get("https://google.com")
        time.sleep(3)

for child_window_id in all_window_ids:
    if child_window_id not in parent_window_id:
        driver.switch_to.window(parent_window_id)
        driver.get("https://apple.com")
        time.sleep(3)

driver.quit()





