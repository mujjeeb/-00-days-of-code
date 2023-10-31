# Day 47 of 100 Days of Code

## Amazon Price Checker

![Amazon Price Checker](https://example.com/amazon_price_checker.jpg)

Welcome to Day 47 of the 100 Days of Code challenge! Today, we introduce the "Amazon Price Checker" – a powerful tool to track the price of your favorite Amazon products. It allows you to set a target price, and if the current price drops below your target, you'll receive an email alert. Let's dive into this project and keep an eye on those amazing deals!

## Project Overview

![Amazon Logo](https://example.com/amazon_logo.jpg)

- **main.py**:
  - The core of the "Amazon Price Checker," this script is highly customizable.
  - You can specify the Amazon product URL and set your target price.
  - The script periodically scrapes Amazon for the current price and compares it to your target.
  - If a price drop is detected, an email alert is sent to notify you of the deal.
  
- **send_email.py**:
  - This module handles the email functionality.
  - You can customize the email subject, message format, and recipient email address.
  - The script uses the `smtplib` library for sending email alerts.

## Getting Started

To set up and run the "Amazon Price Checker" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests bs4 smtplib
     ```

2. **Email Configuration:**
   - In the `send_email.py` module, configure the email sender's credentials, recipient's email address, and the email subject format.

3. **Customization:**
   - In the `main.py` script, customize the project to suit your needs by providing:
     - The Amazon product URL you want to monitor.
     - The target price at which you wish to be alerted.
     - Set the frequency of price checks to match your preferences.

4. **Run the App:**
   - Execute the `main.py` script to start monitoring the Amazon product's price.
   - The script will periodically check and send email alerts if the price drops below your target.

## Usage

- The "Amazon Price Checker" project allows you to track the price of your desired Amazon products and catch the best deals.
- It's a valuable tool for savvy shoppers who want to make sure they don't miss out on discounts.

## Customization

- Customize the script to monitor multiple products or adjust the frequency of price checks.
- Extend the project to support various online stores or add additional notification methods.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational and practical purposes. It helps you automate the process of tracking and catching price drops.


## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy using the "Amazon Price Checker" to find the best deals on Amazon and save on your favorite products! 🛒💰