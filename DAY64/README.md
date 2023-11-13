# Day 64 - Top 10 Movies by Mujjeeb

Welcome to "Top 10 Movies by Mujjeeb," a web application that recommends top movies, fetches details from the movie database API, and allows users to add movies to a local database.

## Overview

"Top 10 Movies by Mujjeeb" leverages `https://api.themoviedb.org/3/search/movie` to recommend top movies and provides users with the ability to add movies to a database based on their selections.

### Project Structure

The project comprises the following structure:

```
top10_movies_by_mujjeeb/
    main.py               # Main Flask application
    templates/            # HTML templates
        index.html         # Displays top recommended movies
        add.html           # Form to search and add movies
    # Any other static resources, if applicable
```

## Project Functionality

### Movie Recommendations

- **Home Page (`index.html`):** Displays a list of top movies recommended by Mujjeeb.

- **Add Movie Page (`add.html`):** Provides a form to search for a movie by name. It fetches a list of similar movie names from the API and allows users to select and add a movie to the database.

- **API Integration:** Utilizes `https://api.themoviedb.org/3/search/movie` to search for movie details and fetch similar movie names based on user input.

### Database Management

- **Adding Movies:** Users can select a movie from the fetched list and add it to the local database, including all its details.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd DAY64
   ```

3. **Install Dependencies:**

   Ensure Flask is installed. If not, install it:

   ```bash
   pip install Flask
   ```

4. **Run the Flask Application:**

   ```bash
   python main.py
   ```

5. **Access the Application:**

   - Open your web browser and go to `http://localhost:5000` to interact with the movie recommendation and adding system.

## Usage

1. **View Top Movies:**
   - Visit the landing page (`index.html`) to view the top recommended movies.

2. **Add a Movie:**
   - Access the `/add` route to search for a movie using the form on the `add.html` page.

3. **Search and Add:**
   - Search for a movie, select it from the list of similar movies, and add it to the local database, capturing all its details.

## Contribution and License

- Contributions to "Top 10 Movies by Mujjeeb" are encouraged. Feel free to fork the repository and submit pull requests for enhancements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Top 10 Movies by Mujjeeb" - Day 64 is developed by Mujjeeb.

Enjoy exploring and adding top movies! For any queries or suggestions, feel free to reach out. Happy movie hunting!