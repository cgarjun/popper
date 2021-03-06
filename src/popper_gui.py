#!/usr/bin/env python
import sys
import argparse
from Tkinter import Tk, Label, Button

WINDOW_TITLE = 'Popper Message !!'

class PopperGui:
    def __init__(self, master, args):
        self.master = master
        master.title(WINDOW_TITLE)

        self.label = Label(master, bg=args.bgcolor, fg='white', text="From: {0}".format(args.sender))
        self.label.pack()

        self.message = Label(master, bg=args.bgcolor, fg='white', text="Message")
        self.message.pack()

        self.body = Label(master, bg=args.bgcolor, wraplength=500, fg='white', text=args.message)
        self.body.pack()

def main(args):
    root = Tk()
    root.minsize(width=500, height=200)
    root.configure(background=args.bgcolor)
    message_gui = PopperGui(root, args)
    root.mainloop()

if __name__ == '__main__':
    arguments = argparse.ArgumentParser("Gui to display the message for chatter")
    arguments.add_argument('--sender', type=str, help='Name / user id of the sender')
    arguments.add_argument('--message', type=str, help='Message from the sender')
    arguments.add_argument('--bgcolor', type=str, default='grey', help='Message display window background color')
    args = arguments.parse_args()
    main(args)