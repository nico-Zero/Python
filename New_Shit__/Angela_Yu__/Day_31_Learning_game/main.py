import customtkinter
from pandas import read_csv, DataFrame
from tkinter import PhotoImage
from random import choice

# -------------------------------------------------------VARIABLES---------------------------------------------------------------
# Display ->
display = customtkinter.CTk()
try:
    data = read_csv(
        "data\\words_to_learn.csv"
    )
except FileNotFoundError:
    data = read_csv("data\\fr_en.csv")
data = data.to_dict(orient="records")


STATE = ["Dark", "Light"]
BACKGROUND_COLOR = "#B1DDC6"

CARD_FRONT = PhotoImage(
    file="images\\card_front.png"
)
CARD_BACK = PhotoImage(
    file="images\\card_back.png"
)

RIGHT = PhotoImage(file="images\\right.png")
WRONG = PhotoImage(file="images\\wrong.png")


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


def start():
    global turn
    display.after_cancel(turn)
    new_word()
    flash_card.itemconfig(card, image=CARD_FRONT)
    flash_card.itemconfig(card_title, text="France:")
    flash_card.itemconfig(card_word, text=france)
    turn = display.after(3000, turn_card)


def turn_card():
    flash_card.itemconfig(card, image=CARD_BACK)
    flash_card.itemconfig(card_title, text="English:")
    flash_card.itemconfig(card_word, text=english)


def right():
    print("Already know", chosen_one)
    data.remove(chosen_one)
    DataFrame(data).to_csv(
        "data\\words_to_learn.csv",
        index=False,
    )
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


# -------------------------------------------------------BUTTON---------------------------------------------------------------
wrong_button = customtkinter.CTkButton(
    master=display,
    text="",
    width=0,
    image=WRONG,
    fg_color=BACKGROUND_COLOR,
    command=wrong,
)
right_button = customtkinter.CTkButton(
    master=display,
    text="",
    width=0,
    image=RIGHT,
    fg_color=BACKGROUND_COLOR,
    command=right,
)

wrong_button.place(x=200, y=535)
right_button.place(x=600, y=535)

turn = display.after(3000, turn_card)
start()
display.mainloop()
