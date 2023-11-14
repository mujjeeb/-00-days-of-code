# Day 66 - Cafe API

Welcome to the "Cafe API," a RESTful API designed to handle cafe-related information using various HTTP verbs.

## Overview

The "Cafe API" project focuses on creating routes for the standard RESTful HTTP verbs (GET, POST, PUT, DELETE) to manage cafe-related data. This API allows users to interact with cafe information programmatically.

### Project Structure

The project comprises the following structure:

```
cafe_api/
    app.py               # Main Flask application defining RESTful routes
```

## Project Functionality

### API Routes

- **GET `/all`:** Retrieves a list of all cafes.

- **GET `/random`:** Retrieves a random cafe.

- **GET `/search?loc=`:** Retrieves the cafe at the provided location.

- **POST `/add`:** Adds a new cafe to the database.

- **PATCH `/update-price/<int:cafe_id>`:** Updates details for a specific cafe by ID.

- **DELETE `/report-closed/<cafe_id>`:** Deletes a specific cafe by ID.

### Data Representation

The API represents cafe information using JSON format, including attributes such as cafe name, location, opening and closing times, coffee strength, WiFi availability, and power availability.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd DAY66
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

5. **Access the API Endpoints:**

   - Use an API testing tool or curl commands to interact with the defined routes (e.g., `GET`, `POST`, `PUT`, `DELETE`).

## API Usage

1. **GET `/all`:**
   - Retrieve a list of all cafes.

2. **GET `/random`:**
   - Retrieves a random cafe.   

3. **GET `/search?loc=`:**
   - Retrieves the cafe at the provided location.

4. **POST `/add`:**
   - Add a new cafe to the database by providing cafe details in the request body.

5. **PUT `/update-price/<int:cafe_id>`:**
   - Update details for a specific cafe by ID. Provide the updated details in the request body.

6. **DELETE `/report-closed/<cafe_id>`:**
   - Delete a specific cafe by ID.

## Contribution and License

- Contributions to the "Cafe API" are welcomed. Fork the repository and submit pull requests for improvements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Cafe API" - Day 66 is developed by Mujjeeb.

Feel free to explore and interact with the Cafe API! For any queries or suggestions, feel free to reach out. Happy coding!