from tkinter import *
import time
import itertools

window = Tk()
window.title("Typing Speed test")
window.geometry("600x300")

sample_text = "In the 16th century, an age of great marine and terrestrial exploration, Ferdinand Magellan led the " \
              "first expedition to sail around the world. As a young Portuguese noble, he served the king of Portugal, " \
              "but he became involved in the quagmire of political intrigue at court and lost the king’s favor. After " \
              "he was dismissed from service by the king of Portugal, he offered to serve the future Emperor Charles V " \
              "of Spain. A papal decree of 1493 had assigned all land in the New World west of 50 degrees W longitude " \
              "to Spain and all the land east of that line to Portugal. Magellan offered to prove that the East Indies " \
              "fell under Spanish authority. On September 20, 1519, Magellan set sail from Spain with five ships. More " \
              "than a year later, one of these ships was exploring the topography of South America in search of a " \
              "water route across the continent. This ship sank, but the remaining four ships searched along the " \
              "southern peninsula of South America. Finally they found the passage they sought near 50 degrees S " \
              "latitude. Magellan named this passage the Strait of All Saints, but today it is known as the Strait of " \
              "Magellan.One ship deserted while in this passage and returned to Spain, so fewer sailors were " \
              "privileged to gaze at that first panorama of the Pacific Ocean. Those who remained crossed the meridian " \
              "now known as the International Date Line in the early spring of 1521 after 98 days on the Pacific " \
              "Ocean. During those long days at sea, many of Magellan’s men died of starvation and disease.Later, " \
              "Magellan became involved in an insular conflict in the Philippines and was killed in a tribal battle. " \
              "Only one ship and 17 sailors under the command of the Basque navigator Elcano survived to complete the " \
              "westward journey to Spain and thus prove once and for all that the world is round, with no precipice at " \
              "the edge. "

sample_text_list = sample_text.split(" ")

# Counters.  i: measures the words in the passage, words_on_screen_counter measures the word on the screen
global i, words_on_screen_counter, timer, CPM, WPM
i = 10
words_on_screen_counter = 0
CPM = 0
WPM = itertools.count(0)

timer = 60
# list of all the words entered by the user
global typed_words
typed_words = []


def timer_clock():
    global timer, i
    timer -= 1
    i = 10
    print(timer)
    change_words('<Button>')
    while timer > -1:
        time_label.config(text=timer)
        restart.config(text="Restart")
        window.update()
        timer -= 1
        time.sleep(1)
    timer = 60
    i = 10
    compute_results()


def compute_results():
    global CPM, WPM
    clean_typed_words = [word for word in typed_words if word != ""]
    print(clean_typed_words)
    [(next(WPM)) for a in sample_text_list for b in typed_words if a == b]
    for a in clean_typed_words:
        for b in sample_text_list:
            if a == b:
                CPM += len(a)
    show_results()

def show_results():
    cpm_label.config(text=f"Corrected CPM: {CPM} ")
    wpm_label.config(text=f"Corrected WPM: {next(WPM)} ")
    text_on_screen.config(text=" ")
    user_entry.delete(0, END)


def change_words(event):
    global i, words_on_screen_counter, typed_words
    words_on_screen_counter += 1
    if words_on_screen_counter % 10 == 0:
        text_on_screen.config(text=f"sample text: {' '.join(sample_text_list[i:(i + 10)])}")
        i += 10
        new_words = user_entry.get().split(" ")
        for word in new_words:
            if word != ' ':
                typed_words.append(word)
        user_entry.delete(0, END)
        # print(typed_words)


# Labels showing the CPM, WPM and time
cpm_label = Label(text="Corrected CPM:  ?")
cpm_label.grid(row=0, column=0)

wpm_label = Label(text="WPM: ?")
wpm_label.grid(row=0, column=1)

time_label = Label(text=timer)
time_label.grid(row=0, column=2)

# Restart Button
restart = Button(text="start", command=timer_clock)
restart.grid(row=0, column=3, padx=10, pady=10)

# Label for sample text
text_on_screen = Label(text=f"sample text: {' '.join(sample_text_list[0:i])}")
text_on_screen.grid(row=1, column=0, columnspan=5, pady=10, padx=10, rowspan=4)

# Entry box
entry_label = Label(text="Your words go here: ")
entry_label.grid(row=6, column=0)
user_entry = Entry(window)
user_entry.grid(row=6, column=1, columnspan=4)
user_entry.bind('<space>', change_words)

window.mainloop()
