import requests
import os
from twilio.rest import Client

account_sid = 'AC23d241c3d059dad56dc84431bcf6d287'
auth_token = os.environ.get('TWILLIO_AUTH_TOKEN')

api_key = os.environ.get('OWM_API_KEY')
weather_parameters = {
    'lat': 	6.465422,
    'lon': 3.406448,
    'exclude': ['current', 'minutely', 'daily', 'alerts'],
    'appid': api_key,
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for n in range(13):
    weather_id = (data['hourly'][n]['weather'][0]['id'])
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an Umbrella, its going to rain 🥶 ☔️",
        from_='[your_twillio_number]',
        to='[recipient number]'
    )
    print(message.status)
else:
    print("You are good to go, there'll be no rain")
