##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import random
import pandas as pd

my_email = "email"
password = "password"

# Save today's month and day 
today = dt.datetime.now()


# Read the birthday csv file to check for birthdays
df = pd.read_csv('birthaday_wisher/birthdays.csv') 



# Check if today is someone's birthday
matching_birthdays = df[(df['month'] == today.month) & (df['day'] == today.day)]

if not matching_birthdays.empty:
    for index, row in matching_birthdays.iterrows():
        name = row['name']
        email = row['email']
        file_path = f"birthaday_wisher/letter_templates/letter_{random.randint(1,3)}.txt"
        print()

        with open (file_path) as letter_file:
            letter_content = letter_file.read()
            letter_content = letter_content.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!!! \n\n {letter_content}")



else:
    print("No one has a birthday today.")