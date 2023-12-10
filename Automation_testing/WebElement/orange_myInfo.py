from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# 1. Login
driver = webdriver.Firefox()
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("Admin")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("admin123")

login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")
login_button.click()

# Verify Login Successfully
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

actual_url = driver.current_url

if expected_url == actual_url:
    print("Login Successful.Test passed")
else:
    print("Login failed.Test failed")

# 3. Go to My Info
my_info = driver.find_element(By.LINK_TEXT, "My Info")
my_info.click()

# 4. Verify My Info page open Successfully
expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"
actual_url = driver.current_url

if expected_url == actual_url:
    print("My Info page open Successful.Test passed")
else:
    print("My Info page not open.Test failed")

time.sleep(4)

# 5. Update First name
first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
first_name.send_keys(Keys.CONTROL, 'a')
first_name.send_keys(Keys.BACKSPACE)
first_name.send_keys("Selenium")

# 6. Select Nationality
nationality = driver.find_element(By.CSS_SELECTOR, ".orangehrm-edit-employee-content "
                                                   ".orangehrm-vertical-padding:nth-of-type(1) "
                                                   ".oxd-grid-item--gutters:nth-of-type(1) [tabindex]")
nationality.click()

# Navigate down to the third option (adjust the count as needed)
for _ in range(3):
    nationality.send_keys(Keys.ARROW_DOWN)

    # Select the option by pressing Enter
    nationality.send_keys(Keys.ENTER)

# Select the option by pressing Enter
nationality.send_keys(Keys.ENTER)

# 7. Select Marital Status
marital_status = driver.find_element(By.CSS_SELECTOR,
                                     ".orangehrm-edit-employee-content .oxd-grid-item--gutters:nth-of-type(2) [tabindex]")
marital_status.click()

# Navigate down to the third option (adjust the count as needed)
for _ in range(2):
    marital_status.send_keys(Keys.ARROW_DOWN)

    # Select the option by pressing Enter
    marital_status.send_keys(Keys.ENTER)

# 8. Enter Date of Birth
dob = driver.find_element(By.CSS_SELECTOR, ".orangehrm-edit-employee-content .oxd-form-row:nth-child(5) [placeholder]")
dob.send_keys(Keys.CONTROL, 'a')
dob.send_keys(Keys.BACKSPACE)
dob.send_keys("2000-10-10")

# 9. Save
save_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-custom-fields .oxd-button--secondary")
save_button.click()

contact_details = driver.find_element(By.LINK_TEXT, "Contact Details")
contact_details.click()
time.sleep(4)


