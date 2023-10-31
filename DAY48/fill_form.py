from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_input = driver.find_element(By.NAME, "fName")
first_name_input.send_keys("John")
last_name_input = driver.find_element(By.NAME, "lName")
last_name_input.send_keys("Doe")
email_input = driver.find_element(By.NAME, "email")
email_input.send_keys("johndoe@gmail.com")
# Using the enter button on the keyboard
# email_input.send_keys(Keys.ENTER)

# Using the enter button on the the webapp

enter_button = driver.find_element(By.CLASS_NAME, "btn")
enter_button.click()

# Close browser window
driver.quit()