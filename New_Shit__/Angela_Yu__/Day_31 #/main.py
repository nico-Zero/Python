import customtkinter
from tkinter import PhotoImage

# -------------------------------------------------------VARIABLES---------------------------------------------------------------
# Display ->
display = customtkinter.CTk()


state = ["Dark", "Light"]
BACKGROUND_COLOR = "#B1DDC6"

CARD_BACK = PhotoImage(file="New_Shit__/Angela_Yu__/Day_31 #/images/card_back.png")
CARD_FRONT = PhotoImage(file="New_Shit__/Angela_Yu__/Day_31 #/images/card_front.png")

RIGHT = PhotoImage(file="New_Shit__/Angela_Yu__/Day_31 #/images/right.png")
WRONG = PhotoImage(file="New_Shit__/Angela_Yu__/Day_31 #/images/wrong.png")


# -------------------------------------------------------CUSTOMTKINTER-SETUPS---------------------------------------------------------------
customtkinter.set_appearance_mode(state := state[0])
display.minsize(width=1000,height=750)
display.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

# -------------------------------------------------------FUNCTIONS---------------------------------------------------------------
def show_back():
    flash_card.itemconfig(card, image=CARD_BACK)

def show_front():
    flash_card.itemconfig(card, image=CARD_FRONT)


# -------------------------------------------------------UI---------------------------------------------------------------


# -------------------------------------------------------CARDS---------------------------------------------------------------
flash_card = customtkinter.CTkCanvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card = flash_card.create_image(400,263,image=CARD_FRONT)
flash_card.place(x=50,y=0)

# -------------------------------------------------------LABEL---------------------------------------------------------------


# -------------------------------------------------------BUTTON---------------------------------------------------------------
right_button = customtkinter.CTkButton(
    text="",
    width=0,
    image=RIGHT,
    highlightthickness=0,
    border=False,
    fg_color=BACKGROUND_COLOR,
    command=show_back
)
wrong_button = customtkinter.CTkButton(
    text="",
    width=0,
    image=WRONG,
    highlightthickness=0,
    border=False,
    fg_color=BACKGROUND_COLOR,
    command=show_front
)
right_button.place(x=200,y=535)
wrong_button.place(x=600,y=535)

display.mainloop()
