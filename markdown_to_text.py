from tkinter import END


def translate_markdown_to_text(markdown, t):
    t.tag_configure("h1", justify='center', font='Courier 16')
    t.tag_configure("h2", justify='center', font='Courier 14')
    t.tag_configure("h3", font='Courier 12')
    t.tag_configure("bold", font="Courier 10 bold")
    t.tag_configure("code", font="Consolas 10 italic", background="black", foreground="white")
    t.tag_configure("code_block", font="Consolas 10", background="black", foreground="white")
    t.tag_configure("blockquote", font="Courier 10", background="grey")

    t.insert(END, markdown)

    replace_remove_start_end(t, "**", "bold")
    replace_remove_start_end(t, "---", "headings")
    replace_remove_start(t, ">", "blockquote")
    replace_remove_start(t, "####", "h3")
    replace_remove_start(t, "##", "h2")
    replace_remove_start(t, "#", "h1")
    replace_remove_start_end(t, "```", "code_block")
    replace_remove_start_end(t, "`", "code")


def replace_remove_start_end(t, chars, tag):
    start, end, char_len = "1.0", "end", len(chars)
    while start > "":
        start = t.search(chars, start, stopindex="end")
        if start:
            end = t.search(chars, f"{start} + {char_len}c", stopindex="end")
            if end:
                end = f"{end} + {char_len}c"
                t.tag_add(tag, start, end)
                t.delete(f"{end} - {char_len}c", end)
                t.delete(start, f"{start} + {char_len}c")
                start = end
            else:
                start = ""


def replace_remove_start(t, chars, tag):
    char_len = len(chars)
    start, end = "1.0", "end"
    while start > "":
        start = t.search(chars, start, stopindex="end")
        if start:
            end = t.search("\n", f"{start} + {char_len}c", stopindex="end")
            if end:
                end = f"{end} + {char_len}c"
                t.tag_add(tag, start, end)
                t.delete(start, f"{start} + {char_len}c")
                start = end
            else:
                start = ""
