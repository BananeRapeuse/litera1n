import sys
import os
import time
from tkinter import *

window = Tk()

window.title("litera1n")
window.geometry('500x450')

def run():
    os.system('python ipwndfu -p')

def term():
    os.system('python term.py')

def exit_app():
    window.quit()

my_frame = Frame(window, width=300, height=300) 
my_frame.pack()

btn = Button(my_frame, text="Jailbreak", bg="black", fg="white", command=run)
btn.place(x=100, y=100, width=100, height=50)

class Lol(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Terminal", command=term)
        fileMenu.add_command(label="Exit", command=exit_app)
        menu.add_cascade(label="Open", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)

class Clock(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=50, y=80)
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.master.after(1000, self.update_clock)

window.configure(bg="black")

# Create instances of the classes
app = Lol(window)
app2 = Clock(window)

window.mainloop()
