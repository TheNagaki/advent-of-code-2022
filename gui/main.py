import importlib
from os.path import exists
from tkinter import *

import requests
from tkinterweb import HtmlFrame

import config
from markdown_to_text import translate_markdown_to_text


def import_right_solution(folder):
    return importlib.import_module(f'{folder}.solution')


def get_input():
    day = get_day()
    fetched_input = get_web_page(f'https://adventofcode.com/2022/day/{day}/input')
    file_to_write = f'../day{day:02}/input.txt'
    if write_input_to_file(fetched_input, file_to_write):
        solution = import_right_solution(f'day{day:02}')
        if not readme_btn.winfo_viewable():
            readme_btn.grid(row=1, column=3)
        swap_text(f'Part 1 : {solution.part1()}\nPart 2 : {solution.part2()}')
        readme_btn.visible = True
    else:
        swap_text('No input for this day')


def get_day():
    day = int(
        "0" + "".join(filter(str.isdigit, day_entered.get())))  # day from input, cleaned from non-digit characters
    return day


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


def get_web_page(url):
    url = url
    headers = {
        'Cookie': 'session=' + config.SESSION_ID
    }
    fetched_input = requests.get(url, headers=headers)
    return fetched_input


def display_readme_as_markdown():
    day = get_day()
    file_path = f'../day{day:02}/README.md'
    if exists(file_path):
        root2 = Tk()
        root2.title('Readme for day ' + str(day))
        root2.geometry('800x600')
        root2.resizable(False, True)
        with open(file_path, 'r') as f:
            readme = f"""{f.read()}"""
        f.close()
        markdown_text = Text(root2, wrap=WORD)
        translate_markdown_to_text(readme, markdown_text)
        markdown_text.pack(expand=True, fill="both")
    else:
        print(f"file {file_path} does not exist")


def display_readme_from_web():
    day = get_day()
    readme_url = f'https://adventofcode.com/2022/day/{day}'
    root2 = Tk()
    root2.title('Readme for day ' + str(day))
    root2.geometry('800x600')
    root2.resizable(False, True)
    text2 = HtmlFrame(root2, horizontal_scrollbar="auto")
    text2.load_website(readme_url)
    text2.pack(expand=True, fill='both')
    root2.mainloop()
    # I cannot yet find a way to display the css properly.


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
compute_result_btn = Button(content_frame, text="Launch", command=get_input)
compute_result_btn.grid(row=0, column=2)
compute_result_btn.grid(padx=1, pady=1)

# Output
text = Text(content_frame, height=2, width=30)
text.grid(padx=1, pady=1)
text.insert(END, "Launch the program to get the solution")
text.tag_configure("center", justify='center')
text.tag_add("center", 1.0, "end")
text.tag_add("italic", 1.0, "end")
text.option_add('*Font', 'TkFixedFont')
text.grid(row=1, column=0, columnspan=3, sticky='nsew')

readme_btn = Button(content_frame, text="?", command=display_readme_from_web)
readme_btn.visible = False
readme_btn.grid(padx=1, pady=1)
readme_btn.grid_forget()
# start the GUI
mainloop()
