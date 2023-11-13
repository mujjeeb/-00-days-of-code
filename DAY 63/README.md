# Day 63 - Personal Library

Welcome to "Personal Library," a project designed to manage and display a collection of books read, showcasing titles, authors, and ratings.

## Overview

"Personal Library" is a book tracking system developed using Flask along with SQLAlchemy for database management. The project presents a list of books read, detailing their title, author, and the rating provided.

### Project Structure

The project comprises the following structure:

```
personal_library/
    main.py               # Main Flask application for handling database
    templates/            # HTML templates
        index.html         # Displays the list of books
        add.html           # Form to add new books
    # Any other static resources, if applicable
```

## Project Functionality

### Database Management

- **Database Creation:** Utilizing Flask-SQLAlchemy, the system manages the database and handles book-related data.

- **Index Page (`index.html`):** Displays the list of books with their titles, authors, and respective ratings.

- **Add Page (`add.html`):** Features a form allowing the addition of new books, gathering book details such as title, author, and rating.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd personal_library
   ```

3. **Install Dependencies:**

   Ensure Flask and SQLAlchemy are installed. If not, install them:

   ```bash
   pip install Flask
   pip install Flask-SQLAlchemy
   ```

4. **Run the Flask Application:**

   ```bash
   python main.py
   ```

5. **Access the Application:**

   - Open your web browser and go to `http://localhost:5000` to interact with your personal book library.

## Usage

1. **View Books:**
   - Visit the landing page (`index.html`) to view the list of books along with their details.

2. **Add a New Book:**
   - Access the `/add` route to input details about a new book via the form on the `add.html` page.

3. **Database Management:**
   - The books and their details are managed and stored within the `books.db` database.

## Contribution and License

- Contributions to "Personal Library" are welcome. Fork the repository and submit pull requests for enhancements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Personal Library" - Day 63 is developed by Mujjeeb.

Enjoy organizing and tracking your read books! For any queries or suggestions, feel free to reach out. Happy reading!