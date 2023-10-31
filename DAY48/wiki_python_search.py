from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# nr_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#
# print(nr_articles.text)
# all_portals = driver.find_element(By.LINK_TEXT, "Donate")
# all_portals.click()

search_for_python = driver.find_element(By.NAME, "search")
search_for_python.send_keys("python")
search_for_python.send_keys(Keys.ENTER)

