
# Day 62 - Coffee and WiFi

Welcome to "Coffee and WiFi," a project that catalogs various cafes along with their details, allowing users to add new entries to the collection. This information is stored in a CSV file for easy retrieval and management.

## Overview

"Coffee and WiFi" serves as a repository for cafes, containing details about each cafe's location, operating hours, coffee strength, WiFi availability, and power availability.

### Project Structure

The project structure includes:

```
coffee_and_wifi/
    main.py               # Main Flask application
    templates/            # HTML templates
        index.html        # Landing page
        cafes.html        # Displays list of cafes
        add.html          # Form to add new cafes
    static/               # Static files
        styles.css        # Custom CSS
```

## Project Functionality

### Routes and Functionality

- **/add Route:** Users can navigate to this route to input details about a new cafe using a form.
- **Cafe Repository:** The data provided in the form is saved into a `cafe-data.csv` file using the `write()` method.
- **Display of Cafes:** The list of cafes is displayed on the `cafes.html` page.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd coffee_and_wifi
   ```

3. **Install Dependencies:**

   Ensure you have Flask installed. If not, install it:

   ```bash
   pip install Flask
   ```

4. **Run the Flask Application:**

   ```bash
   python main.py
   ```

5. **Access the Application:**

   - Open your web browser and go to `http://localhost:5000` to interact with the cafe repository.

## Usage

1. **View Cafes:**
   - Visit the landing page to view the list of cafes.

2. **Add a New Cafe:**
   - Navigate to the `/add` route and complete the form to add a new cafe to the repository.

3. **Cafe Details:**
   - The details added through the form are saved in `cafe-data.csv`.

## Contribution and License

- Contributions to "Coffee and WiFi" are encouraged. Feel free to fork the repository and submit pull requests for improvements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Coffee and WiFi" - Day 62 is developed by Mujjeeb.

Enjoy exploring cafes and adding to the repository! For any queries or suggestions, feel free to reach out. Happy cafe hunting!