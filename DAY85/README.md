#  DAY85 - Watermark App with Tkinter 

This project is a simple watermark application built with Python using the Tkinter library. The application allows users to choose an image, input a text watermark, and then apply the watermark to the selected image. The watermarked image is displayed in the Tkinter window.

## Project Structure

- **main.py:** This is the main Python script containing the code for the watermark application.
- **static/test.jpg:** A sample image used as the default image in the application.
- **static/new_image.jpg:** The output of the watermarked image is saved with this filename.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd DAY85
   ```

3. **Run the Application:**
   ```bash
   python main.py
   ```

4. **Choose an Image:**
   - Click the "Choose Image" button to select any image you want to watermark.

5. **Add Watermark:**
   - Enter the text watermark in the provided entry box.
   - Click the "Add Watermark" button to apply the watermark to the chosen image.

6. **Output:**
   - The watermarked image is displayed in the Tkinter window.
   - The application saves the watermarked image as "static/new_image.jpg."

## Dependencies

Make sure to have the required dependencies installed:

```bash
pip install Pillow
```

## Additional Notes

- The default image path is set to "static/test.jpg." You can modify the `IMG_PATH` variable in the script if needed.
- The application uses the Pillow library (`Image`, `ImageTk`, `ImageFont`, `ImageDraw`) for image processing and Tkinter for the graphical user interface.

## Contribution and License

- Contributions to the project are welcomed. Fork the repository and submit pull requests for improvements.
- The project is licensed under MIT. Refer to the `LICENSE` file for more details.

## Author

This Watermark App with Tkinter is developed by [Author Name]. If you have any questions or suggestions, feel free to reach out. Happy watermarking!