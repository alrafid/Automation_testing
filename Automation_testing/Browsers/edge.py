from selenium import webdriver

# launch the browser
driver = webdriver.Edge()

# URL
driver.get("http://google.com")


# browser close
driver.close()