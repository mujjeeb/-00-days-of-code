# Day 69 - Enhanced Blog with User Registration

Welcome to "Enhanced Blog," an upgraded blog application that now includes user registration, login functionality, and the ability for registered users to comment on and post blogs.

## Overview

"Enhanced Blog" builds upon the previous blog projects, introducing user-specific features to enhance the overall user experience. Now, users can create accounts, log in, comment on posts, and create their blog posts.

### Project Structure

The project structure has been extended to include user-related functionalities:

```
enhanced_blog/
    main.py               # Main Flask application
    templates/          # HTML templates
        index.html       # Home page displaying blog posts
        post.html        # Individual blog post page
        make_post.html    # Form to create a new blog post
        edit_post.html   # Form to edit an existing blog post
        about.html      # About page for the Author
        contact.html    # Contact page 
        #header.html    # Conatains Header elements and style for all pages
        #footer.html    # Conatains Footer elements and style for all pages
        #register.html  # User register page
        #login.html     #User Login page
    static/               # Static files (e.g., CSS, JavaScript)
        styles.css        # Custom styles
```

## Project Functionality

### User Registration and Login

- **Registration Page (`register.html`):** Allows users to create new accounts by providing necessary details.

- **Login Page (`login.html`):** Provides a login form for registered users to log in and access additional features.

### Enhanced Blog Interaction

- **Commenting:** Registered users can comment on blog posts.

- **User-specific Blog Posts:** Users can create their blog posts after logging in.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd enhanced_blog
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

5. **Access the Enhanced Blog:**

   - Open your web browser and go to `http://localhost:5000` to explore the enhanced blog with user registration and login features.

## Usage

1. **Register:**
   - Visit the registration page (`register.html`) to create a new user account.

2. **Login:**
   - Once registered, log in using the login page (`login.html`).

3. **Comment on Posts:**
   - Logged-in users can comment on blog posts.

4. **Create New Blog Posts:**
   - After logging in, users can create their blog posts using the `new_post.html` form.

## Contribution and License

- Contributions to "Enhanced Blog" are encouraged. Fork the repository and submit pull requests for enhancements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"Enhanced Blog" - Day 69 is developed by Mujjeeb.

Enjoy the new features in the blog application! If you have any questions or suggestions, feel free to reach out. Happy blogging!