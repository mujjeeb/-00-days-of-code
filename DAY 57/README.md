# Day 57 of 100 Days of Code

## Simple Blog Site



Welcome to Day 57 of the 100 Days of Code challenge! In today's project, the "Simple Blog Site," we will create a basic blog website that displays blog posts retrieved from a JSON endpoint. This project showcases web development with Python using Flask and HTML templates.

## Project Overview

### Project Structure

- **static**:
  - This directory contains a CSS file (`style.css`) to style the web pages.

- **templates**:
  - This directory includes two HTML templates:
    - `index.html`: The main page that displays a list of blog post previews.
    - `post.html`: The individual blog post page that displays the full content of a selected blog post.

- **main.py**:
  - The "main.py" script is the core of this project.
  - It uses Flask to create a web application and retrieves data from an external JSON endpoint (provided by npoint.io) that contains fake blog posts.
  - The script parses the JSON response and creates post objects with attributes such as title, ID, body, and subtitle.
  - It renders the blog post previews using the `index.html` template.

- **post.py**:
  - This script defines the `Post` class used to create post objects with attributes like title, ID, body, and subtitle.
  - The objects are then used to render individual blog posts on the site.

### Web Pages

- **Home Page (index.html)**:
  - Displays a list of blog post previews, each with a title, subtitle, and a "Read" link.
  - Each "Read" link directs the user to the individual blog post page.

- **Individual Blog Post Page (post.html)**:
  - Displays the full content of a selected blog post, including the title, subtitle, and body.

## Getting Started

To get started with the "Simple Blog Site" project, follow these steps:

1. **Dependencies:**
   - Ensure you have Python installed on your system.
   - Install the required libraries using pip:
     ```bash
     pip install flask requests
     ```

2. **Run the App:**
   - Execute the `main.py` script to start the Flask web application.
   - Access the blog site by navigating to `http://localhost:5000` or `http://127.0.0.1:5000` in a web browser.

## Usage

- The "Simple Blog Site" is a basic yet functional blog website for displaying and reading blog posts.
- Use it as a template to build and customize your blog site or portfolio.

## Customization

- Customize the project by modifying the HTML templates, CSS styles, or adding additional features like comments, search, and user accounts.
- Explore opportunities to extend the project by connecting it to a database or integrating user authentication.

## Credits

This project is part of the 100 Days of Code challenge and is designed for educational and practical purposes. It demonstrates how to create a simple web application for content display.

Enjoy using and enhancing the "Simple Blog Site" project. Share your thoughts and experiences with your readers! 📝🌐😊