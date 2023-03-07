import numpy as np
import random
import tkinter as tk
from tkinter import ttk
import time
import Table

table = None

def randomize_array(size: int) -> list:
    new_array = np.random.randint(0, 10, (size))
    table.show_array(new_array)

def main():
    window = tk.Tk()

    window.title("Lab 5")


    window.geometry('300x300')

    frame = tk.Frame(window)
    frame.pack()

    button = tk.Button(frame, text="Random", command=lambda: randomize_array(10))
    button.pack()

    spinbox_label = tk.Label(frame, text='Choose amount of elements: ')
    spinbox_label.pack()
    spinbox = tk.Spinbox(frame, from_=3, to=100, textvariable=tk.StringVar(frame, '5'))
    spinbox.pack()

    global table
    table = Table.Table(frame)

    randomize_array(10)

    window.bind('q', exit)
    window.mainloop()

if __name__ == '__main__':
    main()