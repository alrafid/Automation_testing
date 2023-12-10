from selenium import webdriver

# launch the browser
driver = webdriver.Firefox()

# URL
driver.get("http://google.com")

# get current page title
current_title = driver.title
print(current_title)

# test
expected_title = "Google"

if expected_title == current_title:
    print("Title matched. Test passed.")
else:
    print("Title not matched. Test failed.")


"""
try:
    # assert
    assert expected_title == current_title
except Exception as e:
    print("Exception raised,Title not matched. Test failed")
"""

# browser close
driver.close()