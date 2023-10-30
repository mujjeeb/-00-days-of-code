# Day 40 of 100 Days of Code

## Flight Deal Project - User Data

Welcome to Day 40 of the 100 Days of Code challenge! Today's project builds upon the "Flight Deal" application from Day 39. In this extended version, we introduce the ability for users to input their first name, last name, and email address, which is then added to a user sheet using the [Sheety API](https://sheety.co/). Let's explore the enhancements.

## Project Overview

The extended "Flight Deal" project consists of the same files as Day 39, plus the following additions:

- **main.py**:
  - This script remains the central hub of the project.
  - It has been enhanced to prompt users to input their first name, last name, and email address.
  - After collecting this information, it calls the `sheety.py` module to add the user's details to a user sheet.

- **sheety.py** (new addition):
  - This module interacts with the Sheety API to add user data to a Google Sheet.
  - It facilitates the process of storing user information for future notifications.

**Note:** Collaborators will need to obtain API keys and authentication credentials for Sheety. You should also set up an additional Google Sheet to store user data and connect it to Sheety.

## Getting Started

To run the extended "Flight Deal" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests twilio
     ```

2. **Configuration:**
   - Open the `main.py` script and provide your API keys and authentication details for Tequila, Sheety, and Twilio.
   - Set up and configure an additional Google Sheet to store user data and connect it to Sheety.

3. **Run the App:**
   - Execute the `main.py` script to start the extended "Flight Deal" app.
   - The script will now prompt users to input their details, which will be added to the user sheet.

## Usage

- The extended "Flight Deal" app allows users to input their information for future flight deal notifications.
- The project now manages both flight deals and user data to enhance the user experience.

## Customization

- Modify the script to add more user input fields or functionalities that align with your project requirements.
- Explore additional features that enhance user engagement and interaction.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational purposes. It helps you learn about integrating external APIs and managing user data in a Google Sheet.

Enjoy using the extended "Flight Deal" project to find great travel deals and engage with users who share the same passion for travel!