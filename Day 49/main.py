from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

USERNAME = os.environ.get('LINKEDIN_USERNAME')
PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3260247296&f_AL=true&f_WT=2%2C3&geoId=105365761&keywords=operations&location=Nigeria&refresh=true&sortBy=R")

sign_in_btn = driver.find_element(By.CSS_SELECTOR, "header nav div .nav__button-secondary")
sign_in_btn.click()

username_input = driver.find_element(By.ID, "username")
username_input.send_keys(USERNAME)

username_input = driver.find_element(By.ID, "password")
username_input.send_keys(PASSWORD)

sign_in_btn = driver.find_element(By.CLASS_NAME, "btn__primary--large")
sign_in_btn.click()
save_job_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_job_btn.click()

driver.quit()