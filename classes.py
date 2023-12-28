from tkinter import ttk


class TextBox(ttk.Entry):
    def __init__(self):
        self.placeholder = placeholder
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)
        print(self.entry)

    def focus_in():
        print("focused in")

    def focus_out():
        print("focused out")
