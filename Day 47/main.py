import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

URL = "https://www.amazon.com/s?k=razer+blade+15%22+gaming+laptop+4k&crid=B6DBS8A30FQD&sprefix=razer+blade+15+gaming+laptop+4k%2Caps%2C728&ref=nb_sb_noss_2"

header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/105.0.0.0 "
                  "Safari/537.36 "
}

response = requests.get(url=URL, headers=header)

EMAIL = os.environ.get("EMAIL_ADDR")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_ADD = "smtp.gmail.com"
BUY_PRICE = 2000

amazon_webpage = response.content


soup = BeautifulSoup(amazon_webpage, "lxml")
price_from_webpage = soup.find(class_="a-offscreen").get_text()
title = soup.find(class_="a-size-medium a-color-base a-text-normal").get_text().strip()

price_without_dollar_sign = (price_from_webpage.strip('$')).replace(',', '')
price = float(price_without_dollar_sign)

print(URL)
print(price)
print(title)

if price < BUY_PRICE:
    message = f"{title} is now ${price}"
    with smtplib.SMTP(SMTP_ADD, port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )







