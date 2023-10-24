import requests
from datetime import datetime
import smtplib
import time

my_email = "email"
password = "password"

MY_LAT = -46.4972
MY_LONG = 156.6439

# function to check if ISS is close
def is_iss_close():
       
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
         return True

     

# Function to check if it's dark enough to see the ISS
def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
         return True


while True:   
    if is_night () and is_iss_close():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="receiverb",
                msg=f"Subject:Possible ISS Sighting\n\n The ISS IS ABOVE.")
    time.sleep(3600)


