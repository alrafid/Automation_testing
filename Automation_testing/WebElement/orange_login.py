from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Go to Login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

# Step 3: Enter/Type Username
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

# step 4: Enter/Type Password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

# step 5: Click Login button
login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
login_button.click()
time.sleep(5)

# step 6: Verify Login as valid
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

actual_url = driver.current_url

if expected_url == actual_url:
    print("Login Successful.Test passed")
else:
    print("Login failed.Test failed")

# step 7: Close browser
driver.close()
