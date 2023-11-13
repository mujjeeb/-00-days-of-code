Certainly! Below is a README for the "Secrets" project that explores Flask, WTForms, and form validation.

# Day 61 - Secrets

Welcome to "Secrets," a project that delves into Flask, WTForms, and WTForms validators to create a simple yet engaging secret-sharing system.

## Overview

"Secrets" is designed to offer users a glimpse into a secret through a sequence of interactions. The project involves multiple pages and form validation to access the secret.

### Project Structure

The project's structure includes:

```
secrets/
    main.py               # Main Flask application
    templates/            # HTML templates
        index.html        # Home page - initial interaction
        login.html        # Login page - for user credentials
        success.html      # Success page - accessed upon correct credentials
        denied.html       # Denied page - for incorrect credentials
    static/               # (if applicable, for static files)
        (assets, CSS, JS)
```

## Project Flow

### Home Page (`index.html`)

Upon arriving at the home page, the user is prompted with a question, asking if they want to know a secret. An affirmative response will lead them to click a button that redirects to the login page.

### Login Page (`login.html`)

The login page requires users to input their email and password. For the test case:

```
USER_EMAIL = "admin@email.com"
USER_PASSWORD = "123456789"
```

### Success Page (`success.html`) and Denied Page (`denied.html`)

- **Success Page:** If the entered credentials match the test case, the user gains access to the success page, displaying the secret with a GIF.
- **Denied Page:** In case of incorrect credentials, the user is redirected to the denied page, also featuring a GIF.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd secrets
   ```

3. **Install Dependencies:**

   It is advisable to have Flask and WTForms installed. If not, install them:

   ```bash
   pip install Flask
   pip install WTForms
   ```

4. **Run the Flask Application:**

   ```bash
   python main.py
   ```

5. **Access the Application:**

   - Open your web browser and go to `http://localhost:5000` to begin the interaction.

## Usage

1. Click to reveal the secret on the home page.
2. Enter the predefined credentials in the login form.
3. If the credentials match, you will be directed to the success page with the secret and GIF.
4. Incorrect credentials will redirect you to the denied page with another GIF.

## Contribution and License

- Contributions to "Secrets" are welcome. Feel free to fork the repository and submit pull requests for enhancements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Secrets" - Day 61 is developed by Mujjeeb.

Explore "Secrets," and enjoy the playful interaction! For any queries or suggestions, feel free to reach out. Happy exploring!