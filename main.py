import importlib
from os.path import exists
from tkinter import *

import requests

import config


def import_right_solution(folder):
    return importlib.import_module(f'{folder}.solution')


def get_input():
    day = int("".join(filter(str.isdigit, day_entered.get())))  # day from input, cleaned from non-digit characters
    fetched_input = get_web_input(day)
    file_to_write = f'../day{day:02}/input.txt'
    if write_input_to_file(fetched_input, file_to_write):
        solution = import_right_solution(f'day{day:02}')
        swap_text(f'Part 1 : {solution.part1()}\nPart 2 : {solution.part2()}')
    else:
        swap_text('No input for this day')


def write_input_to_file(fetched_input, file_to_write):  # if file exists, input is not empty AND request is successful
    if exists(file_to_write) and fetched_input.text != '' and fetched_input.status_code == 200:
        with open(file_to_write, 'w') as f:
            f.write(fetched_input.text)
        f.close()
        return True
    else:
        return False


def swap_text(message):
    text.delete(1.0, END)
    text.insert(END, message)
    text.tag_add("center", 1.0, "end")


def get_web_input(day):
    url = f'https://adventofcode.com/2022/day/{day}/input'
    headers = {
        'Cookie': 'session=' + config.SESSION_ID
    }
    fetched_input = requests.get(url, headers=headers)
    return fetched_input


# GUI
root = Tk()
root.title("Advent of Code 2022")
root.resizable(True, True)
root.geometry("290x80")

# Center the main frame
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)
content_frame = Frame(root)
content_frame.grid(row=1, column=1, sticky='nsew')

content_frame.grid(padx=1, pady=1)
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(1, weight=3)
content_frame.grid_columnconfigure(2, weight=1)

# Inputs
Label(content_frame, text="Day to test :").grid(row=0)
day_entered = Spinbox(content_frame, from_=1, to=25, width=5)
day_entered.grid(row=0, column=1)
day_entered.option_add('*Font', 'TkFixedFont')
b = Button(content_frame, text="Launch", command=get_input)
b.grid(row=0, column=2)
b.grid(padx=1, pady=1)

# Output
text = Text(content_frame, height=2, width=30)
text.grid(padx=1, pady=1)
text.insert(END, "Launch the program to get the solution")
text.tag_configure("center", justify='center')
text.tag_add("center", 1.0, "end")
text.tag_add("italic", 1.0, "end")
text.option_add('*Font', 'TkFixedFont')
text.grid(row=1, column=0, columnspan=3, sticky='nsew')

# start the GUI
mainloop()
