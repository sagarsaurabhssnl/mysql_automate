from tkinter import *
from tkinter import ttk
import time
from threading import Timer


def addA():
    aa.set(int(aa.get())+1)


def timer(func_to_call):
    Timer(1, func_to_call).start()


def calculate(*args):
    try:
        aa.set(0)
        timer(addA)
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Feet to Meters")

login_form = ttk.Frame(root, padding="3 3 12 12")
login_form.grid(column=0, row=0, sticky=(N, W, E, S))


feet = StringVar()
aa = StringVar()
aa.set(0)


timer(addA)

username_entry = ttk.Entry(login_form, width=25, textvariable=feet)
username_entry.insert(0, "Username")
username_entry.pack()
username_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(login_form, textvariable=aa).grid(column=2, row=2, sticky=(W, E))

ttk.Button(login_form, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

ttk.Label(login_form, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(login_form, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(login_form, text="meters").grid(column=3, row=2, sticky=W)

for child in login_form.winfo_children():
    child.grid_configure(padx=5, pady=5)


def returnPressed(*args):
    print("return Presssed")


username_entry.focus()
root.bind("<Return>", returnPressed)

user_id = ttk.Entry(login_form)
root.mainloop()


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()


if __name__ == "__main__":
    root = tk.Tk()
    username = EntryWithPlaceholder(root, "username")
    password = EntryWithPlaceholder(root, "password", 'blue')
    username.pack()
    password.pack()
    root.mainloop()
