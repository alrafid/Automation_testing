from selenium import webdriver

# launch the browser
driver = webdriver.Chrome()

# URL
driver.get("http://google.com")

# browser close
driver.close()