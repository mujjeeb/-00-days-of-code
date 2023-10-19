from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_word = {}

df = pandas.read_csv('./data/french_words.csv')
# next line changes dataframe to dict that returns a list of dictionary
to_learn = df.to_dict(orient="records")



def next_card():
   global current_word
   current_word = random.choice(to_learn)
   canvas.itemconfig(title_text, text = 'French',fill="black")
   canvas.itemconfig(word_text, text= (current_word ['French']), fill="black")
   canvas.itemconfig(card_background, image=card_front_img)
   



def flip_card():
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text= (current_word ['English']), fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    window.after(3000,func=next_card)

def is_known():
    global current_word
    to_learn.remove(current_word)
    flip_card()


# ------ UI setup ------- #

window = Tk()
window.title("Flashy", )
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
title_text = canvas.create_text(400, 150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text="", fill="black", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)




# Know Button
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=0, row=1)


# Dont_know Button
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=flip_card)
wrong_button.grid(column=1, row=1)


# flip_timer = window.after(3000, func=flip_card())
next_card()
window.mainloop()