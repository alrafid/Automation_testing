import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from configparser import ConfigParser


def login_test(email, password):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)

    # Step 2: Go to Login page
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

    # Step 3: Enter/Type Username
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys(email)
    time.sleep(5)

    # step 4: Enter/Type Password
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(password)
    time.sleep(5)

    # step 5: Click Login button
    login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
    login_button.click()

    driver.close()


config_object = ConfigParser()
config_object.read("user_details.ini")

userinfo = config_object["User_info"]
email_data = userinfo["email"]
password_data = userinfo["password"]

login_test(email_data, password_data)

# login_test("email@yahoo.com", "123456")
# login_test("email123@yahoo.com", "123456")
