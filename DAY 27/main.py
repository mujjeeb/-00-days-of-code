from tkinter import *

window = Tk()
window.title("Miles to Km Converter ")
window.config(pady=20, padx=20)


entry = Entry(width=5)
# Gets text in entry

entry.grid(column=2, row=1)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

is_equal_label = Label(text="Miles")
is_equal_label.grid(column=1, row=2)

in_km_label = Label(text="0")

in_km_label.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)


# Buttons
def action():
    miles = float(entry.get())
    km = miles * 1.60934
    km = round(km, 1)
    in_km_label.config(text=f"{km}")


# calls action() when pressed
button = Button(text="Calculate", command=action)
button.grid(column=2, row=3)

window.mainloop()
