# Day 39 of 100 Days of Code

## Flight Deal Finder Project

Welcome to Day 39 of the 100 Days of Code challenge! Today's project is the "Flight Deal" application, which uses the [Tequila API by Kiwi.com](https://tequila-api.kiwi.com) and the [Sheety API](https://sheety.co/) to find and alert you about the cheapest flight deals. Let's get started.

## Project Overview

The "Flight Deal" project consists of multiple files:

- **main.py**:
  - This is the main script that orchestrates the entire project.
  - It interacts with other modules to search for the cheapest flights and send notifications if a deal is found.

- **flight_data.py**:
  - This module contains data about cities and their IATA codes. It populates a Google Sheet with IATA codes using the Sheety API.

- **flight_search.py**:
  - This module interacts with the Tequila API to search for flight deals.
  - It compares the flight prices with the prices listed in the Google Sheet.

- **notification_manager.py**:
  - This module handles notifications. It sends SMS notifications to your specified phone number using the Twilio API if a deal is found.

- **data_manager.py**:
  - This module manages data. It reads and updates data in the Google Sheet using the Sheety API.

**Note:** Collaborators will need to obtain API keys and authentication credentials for Tequila, Sheety, and Twilio. You should also set up your own Google Sheet and connect it to Sheety.

## Getting Started

To run the "Flight Deal" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests twilio
     ```

2. **Configuration:**
   - Open the `main.py` script and provide your API keys and authentication details for Tequila, Sheety, and Twilio.
   - Set up your Google Sheet and connect it to Sheety.
   - Customize your desired cities and IATA codes in the `flight_data.py` module.

3. **Run the App:**
   - Execute the `main.py` script to start the "Flight Deal" app.
   - The script will search for flight deals and notify you if a cheaper deal is found.

## Usage

- The "Flight Deal" app is designed to help you find and stay informed about the best flight deals to your preferred destinations.
- Customize the script with your chosen cities and deal thresholds.

## Customization

- Modify the script to search for flight deals for different cities, adjust the deal thresholds, or add new functionalities based on your travel preferences.

## Credits

This project is part of the 100 Days of Code challenge and is intended for educational purposes. It helps you learn about integrating external APIs and creating a flight deal tracking system.

Enjoy using the "Flight Deal" project to find great travel deals and explore new destinations!