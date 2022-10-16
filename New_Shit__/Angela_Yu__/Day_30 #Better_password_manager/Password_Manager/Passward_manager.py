import customtkinter
from password_generator import pass_gen
from PIL import Image, ImageTk
import pyperclip
import json

# -------------------------------------------------------VARIABLES---------------------------------------------------------------
state = ["Dark", "Light"]
data_file = "New_Shit__/Angela_Yu__/Day_30 #Better_password_manager/Password_Manager/password.json"
image = (
    "New_Shit__/Angela_Yu__/Day_30 #Better_password_manager/Password_Manager/lock.png"
)
customtkinter.set_appearance_mode(state := state[0])


# -------------------------------------------------------FUNCTIONS---------------------------------------------------------------
def all_clear(cf=True):
    if cf:
        config_reset(entry_website)
        config_reset(entry_email)
        config_reset(entry_password)

    entry_website.delete(0, customtkinter.END)
    entry_email.delete(0, customtkinter.END)
    entry_password.delete(0, customtkinter.END)
    clear_info()

    entry_website.focus()


def clear_info():
    info.configure(state=customtkinter.NORMAL)
    info.delete(0, customtkinter.END)
    info.configure(state=customtkinter.DISABLED)

def send_info(message="---"):
    info.configure(state=customtkinter.NORMAL)
    info.insert(customtkinter.END, string=message)
    info.configure(state=customtkinter.DISABLED)


def ok_button():
    clear_info()


def config_red(entry):
    if state == "Light":
        entry.configure(fg_color="#bf4040")
    elif state == "Dark":
        entry.configure(fg_color="#a65974")


def config_reset(entry):
    if state == "Light":
        entry.configure(fg_color="white")
    elif state == "Dark":
        entry.configure(fg_color="#323432")


def search_password():
    with open(data_file, "r") as f:
        website = entry_website.get()
        try:
            data = json.load(f)[website]
        except KeyError:
            clear_info()
            send_info("No such Website name stored.")
            return

    customtkinter.CTkInputDialog(
        title=website, text=f"Email: {data['email']}\nPassword: {data['password']}"
    ).get_input()


def gen_pass_for_password_entry():
    password = pass_gen()

    pyperclip.copy(password)

    config_reset(entry_password)
    config_reset(entry_website)
    config_reset(entry_email)

    entry_password.delete(0, customtkinter.END)
    entry_password.insert(customtkinter.END, string=password)


def add_pass():
    pass_data = [entry_website.get(), entry_email.get(), entry_password.get()]

    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if "" in pass_data:
        clear_info()
        send_info("Don't leave Entry's empty.")
        entry_website.focus() if website == "" else entry_email.focus() if email == "" else entry_password.focus()

        [
            config_red(j) if i == "" else config_reset(j)
            for i, j in zip(pass_data, entry_group)
        ]

    else:
        config_reset(entry_website)
        config_reset(entry_email)
        config_reset(entry_password)

        is_ok = customtkinter.CTkInputDialog(
            title=website, text=f"Email: {email}\nPassword: {password}\nComment:"
        )
        comment = is_ok.get_input()

        if comment != None:
            new_data = {
                website: {
                    "email": email,
                    "password": password,
                    "comment": comment if comment else "---",
                }
            }
            try:
                with open(data_file, "r") as f:
                    data = json.load(f)
                    data.update(new_data)

            except json.decoder.JSONDecodeError:
                with open(data_file, "w") as f:
                    json.dump(new_data, f, indent=4)

            else:
                with open(data_file, "w") as f:
                    json.dump(data, f, indent=4)

            all_clear(cf=False)


# -------------------------------------------------------UI---------------------------------------------------------------

# Window
display = customtkinter.CTk()
display.title("Password Manager")
display.config(padx=20, pady=20)

# Lack Image
img = Image.open(image)
img = ImageTk.PhotoImage(img)
lock_img = customtkinter.CTkLabel(width=144, height=144, borderwidth=0, image=img)

# Labels
top_label = customtkinter.CTkLabel(text="Password", text_font=("Courier", 20))
website = customtkinter.CTkLabel(text="Website :", text_font=("Courier", 12))
email = customtkinter.CTkLabel(text="Username/Email :", text_font=("Courier", 12))
password = customtkinter.CTkLabel(text="Password :", text_font=("Courier", 12))
info_label = customtkinter.CTkLabel(text="Info :", text_font=("Courier", 12))


# EntryBoxes
entry_website = customtkinter.CTkEntry(width=250)
entry_website.focus()
entry_email = customtkinter.CTkEntry(width=400)
entry_password = customtkinter.CTkEntry(width=250)
info = customtkinter.CTkEntry(width=400, state=customtkinter.DISABLED)


entry_group = [entry_website, entry_email, entry_password]

# Buttons
search = customtkinter.CTkButton(
    corner_radius=7,
    text="Search Password",
    highlightthickness=0,
    bg="white",
    border=False,
    command=search_password,
)
generate_password = customtkinter.CTkButton(
    corner_radius=7,
    text="Generate Password",
    highlightthickness=0,
    bg="white",
    border=False,
    command=gen_pass_for_password_entry,
)
add_password = customtkinter.CTkButton(
    width=400,
    corner_radius=8,
    text="Add Password",
    highlightthickness=0,
    bg="white",
    border=False,
    command=add_pass,
)
clear = customtkinter.CTkButton(
    width=140,
    corner_radius=8,
    text="Clear Screen",
    highlightthickness=0,
    bg="white",
    border=False,
    command=all_clear,
)
ok = customtkinter.CTkButton(
    width=140,
    corner_radius=8,
    text="Ok",
    highlightthickness=0,
    bg="white",
    border=False,
    command=ok_button,
)

# Lock Image grid
lock_img.grid(row=0, column=1)

# Labels grids and placing
top_label.grid(row=1, column=1)
website.grid(row=2, column=0)
email.grid(row=3, column=0, pady=5)
password.grid(row=4, column=0)
info_label.place(x=-30, y=375)

# EntryBoxes grids and placing
entry_website.grid(columnspan=1, row=2, column=1)
entry_email.grid(columnspan=2, row=3, column=1, pady=5)
entry_password.grid(columnspan=1, row=4, column=1)
info.place(x=10, y=400)

# Buttons grids and placing
search.grid(row=2, column=2)
generate_password.grid(row=4, column=2)
add_password.grid(columnspan=2, row=5, column=0, pady=5)
clear.grid(row=5, column=2, pady=2)
ok.place(x=420, y=400)

display.mainloop()
