from selenium import webdriver
from selenium.webdriver.common.by import By

# step 1: Launch Browser
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(5)

# Step 2: Go to Login page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")


# Step 3: Enter/Type Username
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("mail@mail.com")

# step 4: Enter/Type Password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

# step 5: Click Login button
login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
login_button.click()
