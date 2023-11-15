# Day 68 - Secrets: A Lesson in Flask Authentication

Welcome to "Secrets," a Flask application showcasing the implementation of user authentication using `flask_login`. This project introduces the concept of user gatekeeping to access a secret file.

## Overview

"Secrets" is designed to teach the fundamentals of Flask authentication, specifically using `flask_login` to manage user sessions. The project focuses on controlling access to a secret file, allowing only authenticated users to view its contents.

### Project Structure

The project comprises the following structure:

```
secrets/
    main.py              # Main Flask application
    templates/           # HTML templates
        login.html        # Login page
        secret.html       # Secret file page
        index.html        # Index page
        base.html         #contaqins base elements for all pages
        register.html     # Register page
    static/               # Static files (e.g., CSS, JavaScript)
        styles.css        # Custom styles
    users.db
```

## Project Functionality

### Authentication with Flask-Login

- **Login Page (`login.html`):** Users are required to log in to access the secret file. Incorrect login attempts are handled gracefully.

- **Secret File Page (`secret.html`):** Once authenticated, users can access the secret file, showcasing the successful implementation of user authentication.

### Flask-Login Integration

- `flask_login` is used to manage user sessions and protect routes, ensuring that only authenticated users can access the secret file.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd DAY68
   ```

3. **Install Dependencies:**

   Ensure Flask and Flask-Login are installed. If not, install them:

   ```bash
   pip install Flask
   pip install Flask-Login
   pip install werkzeug.security
   pip install flask_sqlalchemy
   ```

4. **Run the Flask Application:**

   ```bash
   python main.py
   ```

5. **Access the Application:**

   - Open your web browser and go to `http://localhost:5000` to explore the authentication lesson.

## Usage

1. **Login:**
   - Visit the login page and log in with valid credentials.

2. **Access Secret File:**
   - Once authenticated, access the secret file page to view its contents.

## Contribution and License

- Contributions to "Secrets" are encouraged. Fork the repository and submit pull requests for improvements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Secrets" - Day 68 is developed by Mujjeeb.

Enjoy exploring and learning about Flask authentication! If you have any questions or suggestions, feel free to reach out. Happy coding!