import requests
import customtkinter
from tkinter import PhotoImage

# https://api.kanye.rest
def kanye_quot():
    kanye_quot = requests.get("https://api.kanye.rest")
    kanye_quot.raise_for_status()
    return kanye_quot.json()["quote"]


def speak_kanye():
    can.itemconfig(shit, text=kanye_quot())


display = customtkinter.CTk()

background = PhotoImage(
    file="New_Shit__/Angela_Yu__/Day_33 #API/kanye_quort_api/background.png"
)
button_image = PhotoImage(
    file="New_Shit__/Angela_Yu__/Day_33 #API/kanye_quort_api/kanye.png"
)
bg_color = "#212325"

display.set_appearance_mode("Dark")
display.minsize(width=500, height=700)
display.config(padx=20, pady=20)

# canvas
can = customtkinter.CTkCanvas(width=300, height=414, bg=bg_color, highlightthickness=0)
can.create_image(150, 207, image=background)
shit = can.create_text(
    150, 150, width=200, justify="center", font=("Courier", 20, "bold")
)


# button
kanye_button = customtkinter.CTkButton(
    text="",
    image=button_image,
    bg=bg_color,
    fg_color=bg_color,
    width=0,
    border=False,
    highlightthickness=0,
    command=speak_kanye,
)

# packing stuffs
can.pack()
kanye_button.pack()

display.mainloop()
