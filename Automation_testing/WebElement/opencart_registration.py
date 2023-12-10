import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from configparser import ConfigParser

fake = Faker()

user_details = []

config_object = ConfigParser()

def write_file(file_location, input_text):
    file_obj = open(file_location, "w")
    file_text = file_obj.write(input_text)
    file_obj.close()


def create_user():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)

    password_data = "123456"

    # Step 2: Go to Login page
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

    first_name = driver.find_element(By.NAME, "firstname")
    name = fake.name()
    first_name.send_keys(name)
    # write_file("user_details.txt", name)
    # user_details.append(name)
    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys(fake.name())

    email_field = driver.find_element(By.NAME, "email")
    email = fake.email()
    email_field.send_keys(email)
    # write_file("user_details.txt", email)
    user_details.append(email)
    time.sleep(5)

    telephone = driver.find_element(By.NAME, "telephone")
    telephone.send_keys("323312312")

    password = driver.find_element(By.NAME, "password")
    password.send_keys(password_data)

    confirm_password = driver.find_element(By.NAME, "confirm")
    confirm_password.send_keys(password_data)

    # Select newsletter subscription option
    newsletter_checkbox = driver.find_element(By.CSS_SELECTOR, "label:nth-of-type(1) > input[name='newsletter']")
    newsletter_checkbox.click()

    terms_and_conditions = driver.find_element(By.NAME, "agree")
    terms_and_conditions.click()

    continue_button = driver.find_element(By.CSS_SELECTOR, "input[value='Continue']")
    continue_button.click()

    write_file("user_details.txt", str(user_details))

    config_object["User_info"] ={
        "name": name,
        "email": email,
        "password": password_data
    }
    with open("user_details.ini", "w") as config_file:
        config_object.write(config_file)

    driver.close()


create_user()
