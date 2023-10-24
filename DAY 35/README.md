# Day 35 of 100 Days of Code

## Rain Alert Project

Welcome to Day 35 of the 100 Days of Code challenge! Today's project is the "Rain Alert" app, a Python application that provides weather alerts via SMS if rain or snow is expected. Let's get started.

## Project Overview

The "Rain Alert" project consists of a single file:

- **main.py**:
  - This is the main script that fetches weather data for the day from the [OpenWeatherMap](https://openweathermap.org/) API using the "https://api.openweathermap.org/data/2.5/onecall" endpoint.
  - It also integrates with the Twilio API to send SMS alerts.
  - You will need to provide your own Twilio account details, including your account SID, authentication token, and phone numbers (sender and recipient).
  - Additionally, you need to supply your OpenWeatherMap API details, including the API key and the coordinates for the location you want to monitor for weather conditions.

## Getting Started

To run the "Rain Alert" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests twilio
     ```

2. **Configuration:**
   - Open the `main.py` script and provide your Twilio and OpenWeatherMap details. You can store these details in environment variables for security.
   - Set the latitude and longitude coordinates for the location you want to monitor.
   - Adjust the alert threshold as needed to specify the level of precipitation at which you want to be notified.

3. **Run the App:**
   - Execute the `main.py` script to start the "Rain Alert" app.
   - The app will check the weather conditions and send an SMS alert if rain or snow is expected.

## Usage

- The "Rain Alert" app will automatically check for weather conditions using the OpenWeatherMap API.
- If rain or snow is expected and the precipitation level exceeds your set threshold, an SMS alert will be sent via Twilio.

## Customization

- You can customize the alert threshold in the `main.py` script based on your preferences.
- Modify the Twilio and OpenWeatherMap settings as needed.

## Credits

This project is part of the 100 Days of Code challenge and is intended for educational purposes. You are encouraged to explore, modify, and expand upon it to further your Python programming skills.



## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy using the "Rain Alert" app and stay prepared for changing weather conditions!