# Day 38 of 100 Days of Code

## Workout Tracker

Welcome to Day 38 of the 100 Days of Code challenge! Today's project is a "Workout Tracker" application that interacts with the [Nutritionix API](https://trackapi.nutritionix.com/v2/natural/exercise) and [Sheety API](https://sheety.co/). This project is designed to help you log your workouts in a Google Sheet, complete with columns for date, time, duration, exercise, and calories. Let's dive in.

## Project Overview

The "Workout Tracker" project includes a single file:

- **main.py**:
  - This script prompts the user to enter details about their workout, such as the exercise, duration, and any other relevant information.
  - It uses the Nutritionix API to calculate the number of calories burned during the workout based on the user's input.
  - The script then posts the workout data, including date, time, duration, exercise, and calories, to a Google Sheet that you've created and connected to Sheety.
  - To run this project successfully, you'll need to provide certain user details, Nutritionix credentials, Sheety credentials, and have a corresponding Google Sheet set up and connected to Sheety.

**Note:** Collaborators will need to obtain Nutritionix API credentials and set up their own Sheety-connected Google Sheet.


## Getting Started

To run the "Workout Tracker" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install requests datetime
     ```

2. **Configuration:**
   - Open the `main.py` script and provide your user details (gender, weight, height, age) as well as your Nutritionix and Sheety credentials.
   - Make sure to have a Google Sheet created and connected to Sheety.

3. **Run the App:**
   - Execute the `main.py` script to start the "Workout Tracker" app.
   - You'll be prompted to enter your workout details, and the script will calculate calories and log the workout in your Google Sheet.
```



2. **Configuration:**
   - Open the `main.py` script and provide your user details (gender, weight, height, age) as well as your Nutritionix and Sheety credentials.
   - Make sure to have a Google Sheet created and connected to Sheety.

3. **Run the App:**
   - Execute the `main.py` script to start the "Workout Tracker" app.
   - You'll be prompted to enter your workout details, and the script will calculate calories and log the workout in your Google Sheet.

## Usage

- The "Workout Tracker" app allows you to log your workouts and track your progress.
- Customize the script as needed to add more exercises or functionalities to suit your fitness goals.

## Customization

- Modify the script to include additional exercises, workout parameters, or any other features that align with your workout routine.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational purposes. It helps you explore integrating external APIs and creating a workout tracking system.

## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy using the "Workout Tracker" project to stay on top of your fitness goals and track your workouts!