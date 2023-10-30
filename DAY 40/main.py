
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
notification_manager = NotificationManager()

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "ABV"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

if flight.price < destination["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )

import sheety

print("Welcome to Angela's Flight Club.\n \
We find the best flight deals and email them to you.")

first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()
phone_number = int(input("What is your last name? "))

email1 = "email1"
email2 = "email2"
while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email : ")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")

sheety.post_new_row(first_name, last_name, email1, phone_number)