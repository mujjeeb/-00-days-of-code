# Day 45 of 100 Days of Code

## 100 Movies that You Must Watch

Welcome to Day 45 of the 100 Days of Code challenge! Today's project is a web scraping exercise to fetch data from [Empire Online](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/) and extract "The 100 Greatest Movies." We'll use the `requests` library to make HTTP requests and `BeautifulSoup` (bs4) to parse the HTML content. The scraped data will be saved into a `movies.txt` file.

## Project Overview

- **main.py**:
  - This script is the core of the project. It sends an HTTP request to the specified URL, retrieves the HTML content, and uses BeautifulSoup to parse the page.
  - It then identifies and extracts the list of "The 100 Greatest Movies."
  - Finally, it saves the movie list into a `movies.txt` file.

## Getting Started

To run the "Web Scraping for the 100 Greatest Movies" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests beautifulsoup4
     ```

2. **Configuration:**
   - Open the `main.py` script.
   - The script is already configured to scrape the data from the provided URL.

3. **Run the App:**
   - Execute the `main.py` script to start the web scraping process.
   - The scraped data will be saved in a `movies.txt` file in the same directory.

## Usage

- The "Web Scraping for the 100 Greatest Movies" project is designed to extract a list of the top 100 movies from the specified webpage.
- The extracted data can be used for various purposes, such as creating your own movie list, performing data analysis, or generating recommendations.

## Customization

- You can modify the script to scrape data from other webpages or adapt it for specific data extraction needs.
- Consider enhancing the project by building a web interface, a database, or further analysis of the scraped data.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational purposes. It helps you understand web scraping techniques and how to work with HTML content using Python.

## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy using the "Web Scraping for the 100 Greatest Movies" project to explore and work with movie data!