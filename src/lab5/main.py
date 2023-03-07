import tkinter as tk
from tkinter import ttk
import Table
import task1
import task2

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (Task1, Task2):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(Task1)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class Task1(tk.Frame):
    def randomize_array_01(self):
        self.array = task1.randomize_array_01(self.array_size)
        self.table.show_array(self.array)

    def randomize_array_int0_50(self):
        self.array = task1.randomize_array_int0_50(self.array_size)
        self.table.show_array(self.array)

    def randomize_array_int10(self):
        self.array = task1.randomize_array_int10(self.array_size)
        self.table.show_array(self.array)

    def on_array_size_spinbox_update(self):
        self.array_size = int(self.array_size_spinbox.get())

    def on_k_spinbox_update(self):
        self.k = int(self.k_spinbox.get())
    
    def execute_task(self):
        self.array = task1.shift(self.array, self.k)
        self.table.show_array(self.array)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.array_size = 5
        self.k = 1
        self.array = [0, 0, 0, 0, 0]

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack()

        self.random_button1 = tk.Button(self.buttons_frame, text="Random [0;1]", command=self.randomize_array_01)
        self.random_button1.pack(side='left')
        self.random_button2 = tk.Button(self.buttons_frame, text="Random [-10;10]", command=self.randomize_array_int10)
        self.random_button2.pack(side='left')
        self.random_button3 = tk.Button(self.buttons_frame, text="Random [0;50]", command=self.randomize_array_int0_50)
        self.random_button3.pack(side='left')
        self.execute_button = tk.Button(self.buttons_frame, text="Execute", command=self.execute_task)
        self.execute_button.pack(side='left')
        self.task2_button = tk.Button(self.buttons_frame, text='Task 2 ->', command=lambda : controller.show_frame(Task2))
        self.task2_button.pack(side='left')

        self.array_size_spinbox_label = tk.Label(self, text='Choose amount of elements: ')
        self.array_size_spinbox_label.pack()
        self.array_size_spinbox = tk.Spinbox(self, from_=3, to=100, textvariable=tk.StringVar(self, f'{self.array_size}'), command=self.on_array_size_spinbox_update)
        self.array_size_spinbox.pack()

        self.k_spinbox_label = tk.Label(self, text="Select k:")
        self.k_spinbox_label.pack()
        self.k_spinbox = tk.Spinbox(self, from_=-1000, to=1000, textvariable=tk.StringVar(self, f'{self.k}'), command=self.on_k_spinbox_update)
        self.k_spinbox.pack()

        self.table = Table.Table(self)

class Task2(tk.Frame):
    def on_row_count_spinbox_update(self):
        self.row_count = int(self.row_count_spinbox.get())

    def on_column_count_spinbox_update(self):
        self.column_count = int(self.column_count_spinbox.get())

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.row_count = 2
        self.column_count = 2
        self.matrix = []

        self.row_count_spinbox_label = tk.Label(self, text='Choose amount rows: ')
        self.row_count_spinbox_label.pack()
        self.row_count_spinbox = tk.Spinbox(self, from_=2, to=10, textvariable=tk.StringVar(self, f'{self.row_count}'), command=self.on_row_count_spinbox_update)
        self.row_count_spinbox.pack()

        self.column_count_spinbox_label = tk.Label(self, text='Choose amount of columns: ')
        self.column_count_spinbox_label.pack()
        self.column_count_spinbox = tk.Spinbox(self, from_=2, to=10, textvariable=tk.StringVar(self, f'{self.column_count}'), command=self.on_column_count_spinbox_update)
        self.column_count_spinbox.pack()

        self.task1_button = tk.Button(self, text='<- Task 1', command=lambda: controller.show_frame(Task1))
        self.task1_button.pack()


def main():
    app = App()
    app.title("Lab 5")
    app.geometry('600x600')
    app.bind('q', exit)
    app.mainloop()

if __name__ == '__main__':
    main()