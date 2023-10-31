from bs4 import BeautifulSoup

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# First prt of this project is done in Beautiful Soup: Extracting the price, links, and addresses from Zillow
#
req_headers = {"Please input your browser details"}

ZILLOW_WEBPAGE_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.87007453616974%2C%22east%22%3A-122.30252353076172%2C%22south%22%3A37.68038770085945%2C%22west%22%3A-122.56413546923828%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"
response = requests.get(url=ZILLOW_WEBPAGE_URL, headers=req_headers)

zillow_webpage = response.content

soup = BeautifulSoup(zillow_webpage, 'html.parser')
# print(soup)

# Getting the links for the properties
links_of_properties_full = soup.find_all('a', attrs={'data-test': 'property-card-link'})
links_of_properties = []

for link in links_of_properties_full:
    if "http" not in link['href']:
        full_link = f"https://www.zillow.com{link['href']}"
    links_of_properties.append(full_link)

# Getting the price for the properties
prices_of_properties = []
prices_of_properties_full = soup.find_all('span', attrs={'data-test': 'property-card-price'})
for price in prices_of_properties_full:
    stripped_price = price.get_text().replace('+ 1 bd', '').replace('/mo', '')
    prices_of_properties.append(stripped_price)

# Getting the address for the properties
addresses_of_properties = []
addresses_of_properties_full = soup.find_all('address', attrs={'data-test': 'property-card-addr'})

for address in addresses_of_properties_full:
    stripped_address = address.get_text()
    addresses_of_properties.append(stripped_address)

print(len(prices_of_properties))
print(len(addresses_of_properties))
print(len(links_of_properties))

# Second part of this project is done with selinium; Fill the earlier extracted info into a Google form
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
GOOGLE_FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdHlIxfb86uW0VpUwQDHLV_Vk_urJXMQAfMYKsfFZZ_WCH78w/viewform'


for n in range(len(prices_of_properties)):
    driver.get(GOOGLE_FORM_URL)
    input_address = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_address.send_keys(addresses_of_properties[n])
    input_price = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_price.send_keys(prices_of_properties[n])
    input_link = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input_link.send_keys(links_of_properties[n])
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()
    time.sleep(2)