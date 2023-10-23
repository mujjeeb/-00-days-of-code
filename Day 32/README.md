

```markdown
# Day 32 of 100 Days of Code

## Projects Overview

Today, you'll find two exciting Python projects in this folder:

1. **Quotes Sender** (`quotes_sender`):
    - Inside the `quotes_sender` folder, you will find two files: `main.py` and `quotes.txt`.
    - `main.py` is a script that checks if today is Monday. If it's Monday, it randomly selects a quote from `quotes.txt` and sends it to an email address provided by you.
    - **Configuration:** To use this project, you'll need to provide your Gmail account's email and password in `main.py`. Additionally, you need to specify the recipient's email address.

2. **Birthday Wisher** (`birthday_wisher`):
    - Inside the `birthday_wisher` folder, you will find three files: `main.py`, `birthdays.csv`, and a folder called `letter_templates` that contains three letter templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`).
    - `main.py` is a script that checks if today is someone's birthday, and if so, it randomly selects one of the letter templates and sends a birthday email.
    - `birthdays.csv` contains the details of people's birthdays with the structure: name, email, year, month, day.
    - **Configuration:** To use this project, you need to provide your Gmail account's email and password in `main.py`.

## Getting Started

Before running these projects, make sure you have Python installed on your system. You can install any necessary libraries using pip:

```bash
pip install pandas
pip install random
```

## Usage

1. **Quotes Sender:**
    - Open `quotes_sender/main.py` and provide your Gmail account's email and password.
    - Specify the recipient's email address in the script.
    - Run `main.py` to send a quote on Monday.

2. **Birthday Wisher:**
    - Open `birthday_wisher/main.py` and provide your Gmail account's email and password.
    - Ensure that `birthdays.csv` is correctly populated with the birthday details.
    - Customize the letter templates in the `letter_templates` folder.
    - Run `main.py` to send birthday wishes to recipients.

Remember to use these scripts responsibly and ensure your Gmail account settings allow for less secure apps or generate an App Password for this project.

## Credits

These projects are part of the 100 Days of Code challenge and are designed for educational purposes. You are encouraged to explore, modify, and expand upon them to further your Python programming skills.

Enjoy coding and have fun sending quotes and birthday wishes!
