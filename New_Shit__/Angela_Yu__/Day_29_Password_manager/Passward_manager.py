import customtkinter
from password_generator import pass_gen
from pandas import DataFrame
from PIL import Image, ImageTk
import pyperclip

state = ["Dark", "Light"]
customtkinter.set_appearance_mode(state := state[0])


def all_clear():
    entry_website.delete(0, customtkinter.END)
    entry_email.delete(0, customtkinter.END)
    entry_password.delete(0, customtkinter.END)


def gen_pass_for_password_entry():
    password = pass_gen()

    pyperclip.copy(password)

    config_reset(entry_password)
    config_reset(entry_website)
    config_reset(entry_email)

    entry_password.delete(0, customtkinter.END)
    entry_password.insert(customtkinter.END, string=password)


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


def add_pass():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if website == "" or email == "" or password == "":
        entry_website.focus() if website == "" else entry_email.focus() if email == "" else entry_password.focus()

        if website == "":
            config_red(entry_website)
        else:
            config_reset(entry_website)

        if email == "":
            config_red(entry_email)
        else:
            config_reset(entry_email)

        if password == "":
            config_red(entry_password)
        else:
            config_reset(entry_password)

    else:
        config_reset(entry_website)
        config_reset(entry_email)
        config_reset(entry_password)

        is_ok = customtkinter.CTkInputDialog(
            title=website, text=f"Email: {email}\nPassword: {password}\nComment:"
        )
        comment = is_ok.get_input()

        if comment:
            dataframe = DataFrame(
                {
                    "website": [website],
                    "email": [email],
                    "password": [password],
                    "comment": [comment if comment else "---"],
                }
            )
            dataframe.to_csv(
                "password.csv",
                mode="a",
                index=False,
                header=False,
            )

            entry_website.focus()
            all_clear()


# -------------------------------------------------------UI---------------------------------------------------------------

# Window
display = customtkinter.CTk()
display.title("Password Manager")
display.config(padx=20, pady=20)

# Lack Image
img = Image.open("lock.png")
img = customtkinter.CTkImage(img)
lock_img = customtkinter.CTkLabel(master=display, width=144, height=144, image=img)
lock_img.grid(row=0, column=1)

# Labels
top_label = customtkinter.CTkLabel(
    master=display, text="Password", font=("Courier", 20)
)
website = customtkinter.CTkLabel(master=display, text="Website :", font=("Courier", 12))
email = customtkinter.CTkLabel(
    master=display, text="Username/Email :", font=("Courier", 12)
)
password = customtkinter.CTkLabel(
    master=display, text="Password :", font=("Courier", 12)
)

top_label.grid(row=1, column=1)
website.grid(row=2, column=0)
email.grid(row=3, column=0)
password.grid(row=4, column=0)

# EntryBoxes
entry_website = customtkinter.CTkEntry(master=display, width=400)
entry_website.focus()
entry_email = customtkinter.CTkEntry(master=display, width=400)
entry_password = customtkinter.CTkEntry(master=display, width=250)

entry_website.grid(columnspan=2, row=2, column=1)
entry_email.grid(columnspan=2, row=3, column=1)
entry_password.grid(columnspan=1, row=4, column=1)


# Buttons
generate_password = customtkinter.CTkButton(
    master=display,
    corner_radius=7,
    text="Generate Password",
    command=gen_pass_for_password_entry,
)
add_password = customtkinter.CTkButton(
    master=display,
    width=500,
    corner_radius=8,
    text="Add Password",
    command=add_pass,
)

generate_password.grid(row=4, column=2)
add_password.grid(columnspan=3, row=5, column=0)


display.mainloop()
