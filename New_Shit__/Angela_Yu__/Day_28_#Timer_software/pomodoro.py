import tkinter
from os import system


# -------------------------------------CONSTANTS--------------------------------
COLORS = ["#DD5353", "#B73E3E", "#990066", "#EDDBC0"]

FONT_NAME = "Courier"
WORK_MIN = 25
SEC = 60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15

# -------------------------------------VARIABLE--------------------------------
check_time = 0
time = 1
s = 1

# -------------------------------------TIMER-RESET--------------------------------


def timer_reset(min, sec, x=2):
    global s, time, check_time
    if x > 0 and check_time > 0:

        s *= -1
        time *= -1
        check_time = 0
        check_label.config(text="")

        start_timer()
        window.after(1000, timer_reset, min, sec, x - 1)


# -------------------------------------START-TIMER--------------------------------
def start_timer():
    global s, check_time

    check_time += 1
    if s > 0:
        s *= -1
        if check_time % 8 == 0:
            timer_label.config(text="Break", fg=COLORS[0])
            check_label.config(text="🗸" * int(check_time / 2))
            timer(LONG_BREAK_MIN * SEC, SEC)

        elif check_time % 2 == 0:
            timer_label.config(text="Break", fg=COLORS[2])
            check_label.config(text="🗸" * int(check_time / 2))
            timer(SHORT_BREAK_MIN * SEC, SEC)

        else:
            timer_label.config(text="Work", fg="green")
            timer(WORK_MIN * SEC, SEC)


# -------------------------------------TIMER--------------------------------
def timer(sec, x):
    global s, time, check_time

    if time < 0:
        pass
    else:
        system("cls")

        second = "0" + str(sec % x) if sec % x < 10 else str(sec % x)
        minute = "0" + str(int(sec / x)) if int(sec / x) < 10 else str(int(sec / x))
        canvas_text = minute + ":" + second

        canvas.itemconfig(timer_text, text=canvas_text)
        print(canvas_text)

        if sec >= 0:
            window.after(1000, timer, sec - 1, x)
        else:
            if check_time != 8:
                s *= -1
                start_timer()
            else:
                canvas.itemconfig(timer_text, text="00:00")


# -------------------------------------WINDOW--------------------------------
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=200, pady=100, bg=COLORS[3])

# -------------------------------------LABELS--------------------------------
timer_label = tkinter.Label(
    text="Timer", font=(FONT_NAME, 40, "bold"), fg="green", bg=COLORS[3]
)
timer_label.grid(row=0, column=1)

check_label = tkinter.Label(font=(FONT_NAME, 20, "bold"), fg="green", bg=COLORS[3])
check_label.grid(row=2, column=1)


# -------------------------------------BUTTONS--------------------------------
start = tkinter.Button(
    text="Start",
    bg="white",
    highlightthickness=0,
    border=False,
    command=start_timer,
)
start.grid(row=2, column=0)
reset = tkinter.Button(
    text="Reset",
    bg="white",
    highlightthickness=0,
    border=False,
    command=lambda: timer_reset(WORK_MIN, SEC),
)
reset.grid(row=2, column=2)


# -------------------------------------CANVAS--------------------------------
canvas = tkinter.Canvas(width=200, height=224, bg=COLORS[3], highlightthickness=0)
tomato_image = tkinter.PhotoImage(
    file="tomato.png"
)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canvas.grid(row=1, column=1)

window.mainloop()
system("cls")
