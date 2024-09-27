#!/usr/bin/python3

from curses import wrapper
import curses
import time 

def addnum(num):
    return 20 + 40 + num

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_CYAN)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLUE)

    # RAD_CYAN = curses.color_pair(1)
    BLACK_GREEN = curses.color_pair(2)
    YELLOW_BLUE = curses.color_pair(3)

    window_1 = curses.newwin(1, 20, 10, 10)
    stdscr.addstr("Hello, Wrold!!!")
    stdscr.refresh()

    for i in range(100):
        window_1.clear()
        if i % 2 == 0:
            color = BLACK_GREEN
        else:
            color = YELLOW_BLUE

        window_1.addstr(f"Number:- {i}", color)
        window_1.refresh()

        time.sleep(0.05)

    stdscr.getch()

wrapper(main)


