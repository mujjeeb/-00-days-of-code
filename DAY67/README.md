# Day 67 - RESTful Blog

Welcome to "RESTful Blog," an upgraded blog application that extends the functionality to include new HTTP routes for creating, editing, and deleting blog posts.

## Overview

"RESTful Blog" builds upon the existing blog project, introducing additional routes to enhance the user experience. Now, users can create new blog posts, edit existing posts, and delete posts directly within the blog website.

### Project Structure

The project structure remains similar to the previous blog project:

```
restful_blog/
    app.py              # Main Flask application
    templates/          # HTML templates
        index.html       # Home page displaying blog posts
        post.html        # Individual blog post page
        make_post.html    # Form to create a new blog post
        edit_post.html   # Form to edit an existing blog post
        about.html      # About page for the Author
        contact.html    # Contact page 
        #header.html    # Conatains Header elements and style for all pages
        #footer.html    # Conatains Footer elements and style for all pages
    static/              # Static files (e.g., CSS, JavaScript)
        styles.css       # Custom styles
```

## Project Functionality

### Additional Routes

- **New Post Page (`new_post.html`):** Allows users to create new blog posts by submitting a form with the post's title and content.

- **Edit Post Page (`edit_post.html`):** Enables users to edit existing blog posts. Users can modify the post's title and content using a form.

### Enhanced User Interaction

- Users can now perform a broader range of actions within the blog website, including creating new posts, editing existing posts, and deleting posts.

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd DAY67
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

5. **Access the Blog Website:**

   - Open your web browser and go to `http://localhost:5000` to explore the RESTful blog.

## Usage

1. **View Blog Posts:**
   - Visit the home page (`index.html`) to view a list of blog posts.

2. **Create a New Post:**
   - Click on the "New Post" link to navigate to the `new_post.html` page. Submit the form to create a new blog post.

3. **Edit an Existing Post:**
   - Click on the "Edit" link next to a blog post on the home page (`index.html`). Edit the post on the `edit_post.html` page and submit the form.

4. **Delete a Post:**
   - Click on the "Delete" link next to a blog post on the home page (`index.html`) to delete the post.

## Contribution and License

- Contributions to "RESTful Blog" are welcomed. Fork the repository and submit pull requests for enhancements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

"RESTful Blog" - Day 67 is developed by Mujjeeb.

Explore the upgraded blog features! For any questions or suggestions, feel free to reach out. Happy blogging!