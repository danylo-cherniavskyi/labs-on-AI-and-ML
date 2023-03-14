import sys
import tkinter as tk
from tkinter import ttk
import lab_funcs
import numpy as np

class App(tk.Tk):
    def on_k_spinbox_update(self):
        self.k = int(self.spinbox.get())

    def on_accuracy_button_click(self):
        test_accuracy, training_accuracy = lab_funcs.train(self.k)
        self.textarea.insert('end', f'For k={self.k}: Accuracy on test data: {test_accuracy*100:.2f}%, on training data: {training_accuracy*100:.2f}%\n\n')
        self.assign_colors()

    def on_output_len_button_click(self):
        self.output_len += 2
        np.set_printoptions(edgeitems=self.output_len, linewidth=sys.maxsize)
        self.print_items()
    
    def on_output_amt_button_click(self):
        self.output_amt += 1
        self.print_items()

    def clear_text(self):
        self.textarea.delete('1.0', 'end')

    def print_items(self):
        self.clear_text()
        for i in range(self.output_amt):
            self.textarea.insert("end", f'Pair {i}:\nFirst image:\n{lab_funcs.lfw_pairs_dataset.pairs[i][0]}\nSecond image:\n{lab_funcs.lfw_pairs_dataset.pairs[i][1]}\n\n')
        self.assign_colors()

    def assign_colors(self):
        for (idx, line) in enumerate(self.textarea.get('1.0', 'end').split('\n')):
            if line.find('Pair') != -1:
                line_start = idx
                line_end = line_start
                column_start = line.find('Pair')
                column_end = 'end'
                self.textarea.tag_add('pairlabel', f'{line_start+1}.{column_start}', f'{line_end+1}.{column_end}')
            if line.find('image:') != -1:
                line_start = idx
                line_end = line_start
                column_start = 0
                column_end = 'end'
                self.textarea.tag_add('imagelabel', f'{line_start+1}.{column_start}', f'{line_end+1}.{column_end}')
            if line.find('For k=') != -1:
                line_start = idx
                line_end = line_start
                column_start = 0
                column_end = line.find(':')
                self.textarea.tag_add('klabel', f'{line_start+1}.{column_start}', f'{line_end+1}.{column_end}')

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.k = 1
        self.output_len = 3
        self.output_amt = 1
        np.set_printoptions(edgeitems=self.output_len)

        self.spinbox_frame = tk.Frame(self)
        self.spinbox_label = tk.Label(self.spinbox_frame, text='Enter k: ')
        self.spinbox_label.pack(side='left')
        self.spinbox = tk.Spinbox(self.spinbox_frame, from_=1, to=int(len(lab_funcs.lfw_pairs_dataset.pairs) * 0.75), textvariable=tk.StringVar(self, f'{self.k}'), command=self.on_k_spinbox_update)
        self.spinbox.pack(side='left')
        self.spinbox_frame.pack()

        self.button_frame = tk.Frame(self)

        self.output_len_button = tk.Button(self.button_frame, text="Print more values", command=self.on_output_len_button_click)
        self.output_len_button.pack(side='left')
        self.output_amt_button = tk.Button(self.button_frame, text="Print next", command=self.on_output_amt_button_click)
        self.output_amt_button.pack(side='left')
        self.accuracy_button = tk.Button(self.button_frame, text="Estimate accuracy", command=self.on_accuracy_button_click)
        self.accuracy_button.pack(side='left')

        self.button_frame.pack()

        self.textarea = tk.Text(self, wrap='none')
        self.textarea.tag_configure("pairlabel", background='magenta')
        self.textarea.tag_configure("imagelabel", background='green')
        self.textarea.tag_configure("klabel", background='cyan')

        self.textarea.pack()
        self.print_items()


def main():
    app = App()

    app.title("Lab 6")
    app.geometry("700x600")
    app.bind('q', exit)
    app.mainloop()

if __name__ == '__main__':
    main()
