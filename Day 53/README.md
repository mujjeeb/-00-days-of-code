# Day 53 of 100 Days of Code

## Zillow Data Gathering

![Zillow Data Gathering](https://example.com/zillow_data_gathering.jpg)

Welcome to Day 53 of the 100 Days of Code challenge! In today's project, "Zillow Data Gathering," we will automate the process of collecting property data from Zillow's rental listings in San Francisco. The goal is to scrape address, price, and link information and then fill out a Google Form to organize the data efficiently.

## Project Overview

- **main.py**:
  - The "Zillow Data Gathering" script is the core of this project.
  - It utilizes web scraping with BeautifulSoup and requests to:
    - Access Zillow's rental listings for San Francisco using a specific search URL.
    - Extract property information, including address, price, and listing link.
  - The script then uses the Google Forms API to:
    - Open a Google Form and fill it with the extracted property data.

## Getting Started

To get started with the "Zillow Data Gathering" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install beautifulsoup4 requests 
     ```

2. **Google API Setup:**
   - You will need to create a Google Form that matches the data you want to collect. Obtain the form's URL.
   - Set up the Google Sheets API and create a service account key file, which you will use for authentication.

3. **Customization:**
   - In the `main.py` script, you can customize the project by:
     - Modifying the Zillow search URL to target specific criteria (e.g., location, price range, number of bedrooms).
     - Specifying the Google Form URL and the field names for address, price, and link.
     - Providing the path to your service account key file for Google Sheets API authentication.

4. **Run the App:**
   - Execute the `main.py` script to initiate the data gathering process.
   - The script will scrape Zillow for property information and fill out the Google Form.

## Usage

- The "Zillow Data Gathering" project is a powerful tool for collecting property data from Zillow listings and efficiently organizing it in a Google Form.
- Use it to track property listings, analyze rental market trends, or streamline your property search.

## Customization

- Customize the script to target specific Zillow listings and Google Form fields that match your data collection needs.
- Explore opportunities to extend the project with additional features, such as automatic data analysis or integration with other platforms.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational and practical purposes. It demonstrates how automation can simplify data collection and organization.

Enjoy data gathering with the "Zillow Data Gathering" project. Make informed property decisions with ease and efficiency! 🏡📊🔍