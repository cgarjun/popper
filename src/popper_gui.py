#!/usr/bin/env python
import sys
import argparse
from tkinter import Tk, Label, Button

class PopperGui:
    def __init__(self, master, sender, message):
        self.master = master
        master.title("Popper Message")

        self.label = Label(master, text="From: {0}".format(sender))
        self.label.pack()

        self.message = Label(master, text="From: {0}".format(message))
        self.message.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Greetings!")

def main(args):
    root = Tk()
    my_gui = PopperGui(root, args.sender, args.message)
    root.mainloop()

if __name__ == '__main__':
    arguments = argparse.ArgumentParser("Gui to display the message for chatter")
    arguments.add_argument('--sender', type=str, help='Name / user id of the sender')
    arguments.add_argument('--message', type=str, help='Message from the sender')
    args = arguments.parse_args()
    main(args)