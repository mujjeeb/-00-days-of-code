
# Day 33 of 100 Days of Code

## Projects Overview

Today, you'll find two Python projects in this folder:

### Project 1: Kanye Quotes (`kanye_quotes`)

- **Files:** `background.png`, `kanye.png`, and `main.py`.
- **Description:** This project fetches random Kanye West quotes from [https://api.kanye.rest](https://api.kanye.rest) and displays them on a Tkinter canvas alongside an image of Kanye West. It's a fun way to get some words of wisdom from the famous rapper.

### Project 2: ISS Overhead (`iss_overhead`)

- **Files:** `main.py`.
- **Description:** This project provides functionality to check the International Space Station (ISS) location and visibility. It includes two functions:
  - `is_iss_close`: Checks if the ISS is close to your location by using data from the [http://api.open-notify.org/iss-now.json](http://api.open-notify.org/iss-now.json) API.
  - `is_night`: Determines if it's dark enough to see the ISS by using sunrise and sunset data from [https://api.sunrise-sunset.org/json](https://api.sunrise-sunset.org/json).
  - A while loop in `main.py` runs with a `time.sleep(3600)` to periodically check the ISS's status and visibility every hour.

## Getting Started

To run these projects, follow these steps:

1. **Kanye Quotes (`kanye_quotes`):**
    - Make sure you have Python installed.
    - Install the required libraries using pip:
      ```bash
      pip install requests
      ```
    - Run `main.py` to get and display random Kanye West quotes with the associated image.

2. **ISS Overhead (`iss_overhead`):**
    - Ensure you have Python installed.
    - Install the required libraries using pip:
      ```bash
      pip install requests
      ```
    - Run `main.py`. It will continuously check for the ISS's proximity and visibility.

## Notes

- Ensure that your internet connection is active to fetch data from the APIs.
- For the `kanye_quotes` project, you can customize the appearance of the Tkinter canvas and the layout of the Kanye image and quotes.

## Credits

These projects are part of the 100 Days of Code challenge and are designed for educational purposes. You are encouraged to explore, modify, and expand upon them to further your Python programming skills.

## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy coding and have fun with Kanye's quotes and tracking the ISS overhead!
