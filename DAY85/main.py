from tkinter import *
from PIL import ImageTk, Image, ImageFont, ImageDraw
from tkinter import filedialog
import os

IMG_PATH = "static/test.jpg"

# This is the directory where the images are usually stored on the users' computer (dependent on the user)
STARTING_DIR = os.environ.get('STARTING_DIR')

window = Tk()
window.title("Watermark App")
window.geometry("300x400")


def add_watermark():
    # get the sentence typed by the user
    text = watermark_entry.get()
    print(text)

    # Open the image
    new_image = Image.open(window.filename)

    draw = ImageDraw.Draw(new_image)

    # font to be used and size
    fnt = ImageFont.truetype("arial.ttf", 30)

    draw.text((5, 5), text, fill="red", font=fnt, align="right")

    # Save new image
    watermark_entry.delete(0, END)
    watermark_entry.insert(0, "Saving file ...")
    new_image.save("static/new_image.jpg")

    picture.after(2000, show_output)


def show_output():
    global new_image
    new_img = Image.open("static/new_image.jpg")
    new_img_resized = new_img.resize((200, 200), Image.Resampling.LANCZOS)
    new_image = ImageTk.PhotoImage(new_img_resized)
    new_img.show()
    picture.config(image=new_image)

    # Clear the entry box
    watermark_entry.delete(0, END)


# A dialog box asking users to choose the images they want to watermark
def choose_image():
    global window
    window.filename = filedialog.askopenfilename(initialdir=STARTING_DIR, title="Select a file",
                                                  filetypes=(("jpeg files", "*.jpeg"), ("png files", "*.png")))
    print((window.filename))
    # Resizing image
    original_img = Image.open(window.filename)
    img_resized = original_img.resize((200, 200), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img_resized)

    # Create label for image
    global picture
    picture = Label(window, image=img)
    picture.grid(row=1, column=1, columnspan=4, pady=20, padx=10)


# Create entry box for the content of the watermark
watermark_label = Label(text="Add text")
watermark_label.grid(row=2, column=1, padx=10)
watermark_entry = Entry(window)
watermark_entry.grid(row=2, column=2, columnspan=1, pady=20)

# Create the button to choose an image
choose_button = Button(text="Choose Image", command=choose_image)
choose_button.grid(row=3, column=1, columnspan=4)

# Create the button to add watermark
button = Button(text="Add Watermark", command=add_watermark)
button.grid(row=4, column=1, columnspan=4)

window.mainloop()
