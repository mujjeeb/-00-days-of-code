# Day 36 of 100 Days of Code

## Stock News Alert Project

Welcome to Day 36 of the 100 Days of Code challenge! Today's project is the "Stock News Alert" app, a Python application that provides stock price and news alerts via SMS. Let's dive in.

## Project Overview

The "Stock News Alert" project consists of a single file:

- **main.py**:
  - This is the main script that:
    - Utilizes the [Alpha Vantage](https://www.alphavantage.co/) API to fetch the closing price of a specified stock (for example, "META") for the last two days.
    - Calculates the percentage difference in the stock's closing price between these two days.
    - If the absolute percentage difference is more than 2%, it fetches the three most recent news articles related to the stock using the [News API](https://newsapi.org/).
    - It formats the article headlines and brief descriptions into a text message alongside the percentage difference in the stock price.
    - Sends this message via [Twilio](https://www.twilio.com/).

**Note:** Collaborators need to obtain API keys and authentication credentials for Alpha Vantage, News API, and Twilio. Additionally, they should provide the recipient's phone number.

## Getting Started

To run the "Stock News Alert" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests twilio
     ```

2. **Configuration:**
   - Open the `main.py` script and provide your API keys and authentication details for Alpha Vantage, News API, and Twilio.
   - Specify the stock symbol (e.g., "META") and the company name (e.g., "Facebook") that you want to monitor.

3. **Run the App:**
   - Execute the `main.py` script to start the "Stock News Alert" app.
   - The app will fetch stock price data, calculate the percentage difference, and send an SMS alert with news articles if the threshold is exceeded.

## Usage

- The "Stock News Alert" app continuously monitors the stock's performance and sends alerts when significant changes occur.
- Collaborators can customize the stock symbol, company name, and alert threshold to match their preferences and investment strategies.

## Customization

- Modify the stock symbol, company name, and percentage threshold as needed.
- You can also adjust the frequency of monitoring, response format, and additional features based on your requirements.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational purposes. Collaborators are encouraged to explore, modify, and expand upon it to enhance their Python programming skills and stay informed about stock market developments.


## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy using the "Stock News Alert" app to keep track of your investments!