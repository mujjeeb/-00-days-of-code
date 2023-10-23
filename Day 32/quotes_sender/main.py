import smtplib
import datetime as dt
import random

my_email = "email"
password = "password"


now = dt.datetime.now()

day_of_the_week = now.weekday()



if day_of_the_week == 0:
    with open('quotes_sender/quotes.txt') as quote_file:
        print(now)
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)


    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="receiverb",
            msg=f"Subject:Hello\n\n {quote}")
