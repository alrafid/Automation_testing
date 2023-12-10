import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.delete_all_cookies()

driver.add_cookie({
    "name": "orangehrm",
    "value": "16f2e7fb516fd2092fea00c6e4a64d53"
})

time.sleep(5)

driver.refresh()