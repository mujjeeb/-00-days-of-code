# MyPass Password Manager (Upgraded)

## Project Overview

**MyPass** is an upgraded user-friendly Python-based password manager that allows you to securely store and manage your website login credentials, including website URLs, usernames, and passwords. The project utilizes the Tkinter library to create an intuitive and secure user interface with the addition of a search feature. It provides the convenience of storing, retrieving, and searching for login information for various websites while ensuring the security of your sensitive data.

## Project Structure

The project is organized as follows:

- **100-days-of-code/DAY 30 Folder**: This folder contains the upgraded project files and resources.
  - `main.py`: The main Python script that runs the MyPass Password Manager with the search feature.
  - `logo.png`: An image file used in the GUI interface.
  - `data.json`: A JSON file where the encrypted login credentials are stored. (Upgraded from `data.txt` for added functionality)
  - `README.md`: The project README file.

## How It Works

To use the **MyPass Password Manager (Upgraded)**:

1. Run the `main.py` script.

2. The GUI interface will open, displaying options to add a new website entry, view existing entries, and search for specific websites.

3. To add a new website entry, click the "Add" button. You can enter the website URL, username, and password for the new entry. The data will be securely encrypted and stored in the `data.json` file.

4. To view your existing entries, click the "View" button. The program will retrieve and display the login information for all saved websites, allowing you to see your website URLs and usernames (passwords are concealed for security).

5. To search for a specific website entry, click the "Search" button and enter the website URL you are looking for. The program will display the corresponding username and allow you to reveal the password.

6. All login information is securely encrypted, and only you can access and decrypt it with the master password that you create during the initial setup.

7. You can also click the "Generate Password" button to create a secure and random password for new website entries.

## Prerequisites

To run the **MyPass Password Manager (Upgraded)**, you need to have Python installed on your system. Tkinter is included in the standard Python library, so there is no need for additional installations.

## Getting Started

To start using the **MyPass Password Manager (Upgraded)**:

1. Clone this project repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/100-days-of-code.git
   ```

2. Change your working directory to the `DAY 30` folder:

   ```bash
   cd 100-days-of-code/DAY\ 30
   ```

3. Run the Python script, `main.py`, to start the MyPass Password Manager with the added search feature:

   ```bash
   python main.py
   ```

4. Use the GUI interface to manage, securely store, retrieve, and search for your website login credentials.

## Example Usage

Here's an example of how the **MyPass Password Manager (Upgraded)** works:

1. Open the GUI interface by running `main.py`.

2. Click the "Add" button to add a new website entry. Enter the website URL, username, and password.

3. Click the "Generate Password" button to create a secure and random password for the new entry.

4. Click the "View" button to see all existing website entries, including website URLs and usernames.

5. Click the "Search" button to search for a specific website entry by entering the website URL. You can reveal the password for that entry if needed.

6. Your login information is securely stored and encrypted in the `data.json` file. You can only access it by entering the master password during the initial setup.


## Contribution and Feedback

Contributions are welcomed to help uncover more insights into the data and deepen my knowledge of Postgre SQL. Feel free traise issues, or provide feedback to help us improve the project.


## Github profile
https://github.com/mujjeeb

Enjoy using the **MyPass Password Manager (Upgraded)** to securely store, manage, and search for your website login credentials with added functionality!
