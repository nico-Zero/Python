import customtkinter
from pandas import read_csv
from tkinter import PhotoImage
from random import choice

# -------------------------------------------------------VARIABLES---------------------------------------------------------------
# Display ->
display = customtkinter.CTk()

data = read_csv("New_Shit__/Angela_Yu__/Day_31 #Learning_game/data/fr_en.csv")
data = data.to_dict(orient="records")

chosen_one = choice(data)
france = chosen_one["France"].lower()
english = chosen_one["English"].lower()

STATE = ["Dark", "Light"]
BACKGROUND_COLOR = "#B1DDC6"

CARD_FRONT = PhotoImage(
    file="New_Shit__/Angela_Yu__/Day_31 #Learning_game/images/card_front.png"
)
CARD_BACK = PhotoImage(
    file="New_Shit__/Angela_Yu__/Day_31 #Learning_game/images/card_back.png"
)

RIGHT = PhotoImage(file="New_Shit__/Angela_Yu__/Day_31 #Learning_game/images/right.png")
WRONG = PhotoImage(file="New_Shit__/Angela_Yu__/Day_31 #Learning_game/images/wrong.png")


# -------------------------------------------------------CUSTOMTKINTER-SETUPS---------------------------------------------------------------
customtkinter.set_appearance_mode(STATE := STATE[0])
display.title("Flash-Game")
display.minsize(width=1000, height=750)
display.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# -------------------------------------------------------FUNCTIONS---------------------------------------------------------------
def new_word():
    global france, english, chosen_one

    chosen_one = choice(data)
    france = chosen_one["France"].lower()
    english = chosen_one["English"].lower()


def turn_card(sec=3):
    if sec != 0:
        display.after(1000, turn_card, sec - 1)
    else:
        flash_card.itemconfig(card, image=CARD_BACK)
        flash_card.itemconfig(card_title, text="English:")
        flash_card.itemconfig(card_word, text=english)

        wrong_button.configure(state=customtkinter.NORMAL)
        right_button.configure(state=customtkinter.NORMAL)
        new_word()


def start():
    flash_card.itemconfig(card, image=CARD_FRONT)
    flash_card.itemconfig(card_title, text="France:")
    flash_card.itemconfig(card_word, text=france)

    wrong_button.configure(state=customtkinter.DISABLED)
    right_button.configure(state=customtkinter.DISABLED)
    turn_card()


def right():
    print("Already know", chosen_one)
    data.remove(chosen_one)
    start()


def wrong():
    print("Don't know", chosen_one)
    start()


# -------------------------------------------------------UI---------------------------------------------------------------


# -------------------------------------------------------CARDS---------------------------------------------------------------
flash_card = customtkinter.CTkCanvas(
    width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0
)
card = flash_card.create_image(400, 263, image=CARD_FRONT)
card_title = flash_card.create_text(
    400, 150, justify="center", font=("Courier", 40, "italic")
)
card_word = flash_card.create_text(
    400, 263, justify="center", font=("Courier", 60, "bold")
)
flash_card.place(x=50, y=0)

# -------------------------------------------------------LABEL---------------------------------------------------------------


# -------------------------------------------------------BUTTON---------------------------------------------------------------
wrong_button = customtkinter.CTkButton(
    text="",
    width=0,
    image=WRONG,
    highlightthickness=0,
    border=False,
    fg_color=BACKGROUND_COLOR,
    command=wrong,
)
right_button = customtkinter.CTkButton(
    text="",
    width=0,
    image=RIGHT,
    highlightthickness=0,
    border=False,
    fg_color=BACKGROUND_COLOR,
    command=right,
)

wrong_button.place(x=200, y=535)
right_button.place(x=600, y=535)

start()
display.mainloop()
