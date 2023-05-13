from os import system
from tkinter import Tk, Button, Label, Entry

system("clear")

# window
window = Tk()
window.title("Mile to kilo")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

# Function for calculating the mile to kilo
def mile_to_kilo(mile):
    try:
        if mile == "clear":
            system("clear")
            labels[3]["text"] = " "
            return None

        elif mile == "":
            labels[3]["text"] = " "

        elif mile:
            mile = int(mile)
            print(round(mile * 1.609344,2))
            labels[3]["text"] = round(mile * 1.609344,2)
    except:
        pass


# Labels
labels = [Label() for i in range(4)]

labels[2]["text"] = "is equal to"
labels[2].grid(row=1, column=0)

labels[0]["text"] = "Miles"
labels[0].grid(row=0, column=2)

labels[1]["text"] = "Km"
labels[1].grid(row=1, column=2)

labels[3]["text"] = None
labels[3].grid(row=1, column=1)

# Entry
mile = Entry(width=7)
mile.grid(row=0, column=1)

# Button
calculate = Button(text="Calculate", command=lambda: mile_to_kilo(mile.get()))
calculate.grid(row=2, column=1)

window.mainloop()
