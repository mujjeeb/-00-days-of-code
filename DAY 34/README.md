
# Day 34 of 100 Days of Code

## Quizzler App

Welcome to Day 34 of the 100 Days of Code challenge! Today's project is the "Quizzler" app, a Python application that allows users to test their knowledge with a series of multiple-choice questions. Let's dive into the details.

## Project Overview

The "Quizzler" app is divided into several files, each serving a specific purpose:

1. **main.py**:
   - The main script to run the Quizzler app. It combines the functionalities provided by other modules to create the quiz.

2. **data.py**:
   - This module fetches questions from the "https://opentdb.com/api.php" API, which serves as the source of questions for the quiz.

3. **question_model.py**:
   - Defines the `Question` class, which represents a single question along with it's answer.

4. **quiz_brain.py**:
   - Contains the `QuizBrain` class that manages the quiz logic, keeps track of the score, and advances through questions.

5. **ui.py**:
   - Implements the user interface for the Quizzler app using Tkinter, allowing users to interact with the quiz. There's a True and False button. and the page illuminates red or green to indicate the correctness of the user's answers.

6. **images** (folder):
   - Contains the images used in the app, including `false.png` and `true.png` for indicating the correctness of user answers.

## Getting Started

To run the Quizzler app, follow these steps:

1. **Dependencies:**
   - Make sure you have Python installed on your system.
   - You might need to install the requests library using pip:
     ```bash
     pip install requests
     ```

2. **Run the App:**
   - Execute the `main.py` script to start the Quizzler app.
   - You will be presented with a series of multiple-choice questions, and you can select your answers.

## Usage

- Answer each question by clicking on your choice (True or False).
- Your score is displayed at the end of the quiz.
- The app fetches questions from an online source, so you can enjoy an ever-changing set of questions.

## Customization

- You can customize the appearance and layout of the app by modifying the UI code in `ui.py`.
- If you want to use a different source for questions, you can adapt the `data.py` module to fetch questions from another API.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational purposes. Feel free to explore, modify, and expand upon it to enhance your Python programming skills.

Enjoy testing your knowledge with the Quizzler app!
