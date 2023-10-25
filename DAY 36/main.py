STOCK = "META"
COMPANY_NAME = "Facebook"


import requests
import os
from twilio.rest import Client

from datetime import datetime, timedelta

today = datetime.today()
yesterday = (today - timedelta(days=1)).strftime('%Y-%m-%d')
the_day_before_yesterday = (today - timedelta(days=2)).strftime('%Y-%m-%d')


## STEP 1: Use  
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
stock_url = 'https://www.alphavantage.co/query?'
stock_response = requests.get(stock_url, params=stock_parameters)
stock_data = stock_response.json()


# Get the close prices of yesterday and the day before that
yesterday_close = float(stock_data['Time Series (Daily)'][yesterday]['4. close'])
the_day_before_yesterday_close = float(stock_data['Time Series (Daily)'][the_day_before_yesterday]['4. close'])



# Checking the percentage change in closing prices
percentage_change = ((yesterday_close - the_day_before_yesterday_close) / yesterday_close) * 100
print(percentage_change)
if percentage_change > 0:
    up_down = "🔺"
elif percentage_change < 0:
    up_down = "🔻"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percentage_change) > 0.001:
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
    news_parameters = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }
    news_url = 'https://newsapi.org/v2/everything?q'
    news_response = requests.get(news_url, params=news_parameters)
    news_data = news_response.json()
    articles = news_data['articles']
    three_articles = articles[:3]
    print(articles)

    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    formatted_articles = [f"{STOCK}: {up_down} {round(abs(percentage_change))} \nHeadline: {article['title']}. \n Brief:{article['description']}" for article in
                          three_articles]

    twillio_account_sid = 'AC23d241c3d059dad56dc84431bcf6d287'
    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(twillio_account_sid, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
            .create(
            body=article,
            from_='+17817256956',
            to='[RECIPIENT NUMBER]'
        )



