from tkinter import ttk
import numpy as np

class Table:
    def __resize_table(self, col_num: int):
        self.__table['columns'] = [num for num in range(col_num)]

    def show_array(self, array: list):
        self.__resize_table(len(array))

        for (idx, el) in enumerate(array):
            self.__table.heading(idx, text=f'{idx}', anchor='center')
            self.__table.column(idx, anchor='center', width=10)
        if len(self.__table.get_children()) > 0:
            self.__table.delete(self.__table.get_children()[0])
        self.__table.insert('', 0, text='', values=tuple(array))

    def show_matrix(self, matrix: np.ndarray):
        self.unhighlight()
        self.__resize_table(len(matrix.max(0)))

        for (idx, el) in enumerate(matrix.max(0)):
            self.__table.heading(idx, text=f'{idx}', anchor='center')
            self.__table.column(idx, anchor='center', width=10)

        while len(self.__table.get_children()) > 0:
            self.__table.delete(self.__table.get_children()[0])
        np.apply_along_axis(lambda row: self.__table.insert('', 'end', text='', values=tuple(row), tags=(self.__determine_tag(matrix, row))), axis=1, arr=matrix)

    def __determine_tag(self, matrix: np.ndarray, row: np.ndarray) -> str:
        row_max = matrix[matrix.max(1).argmax()]
        row_min = matrix[matrix.min(1).argmin()]

        if np.array_equal(row, row_max):
            return 'max_row'

        if np.array_equal(row, row_min):
            return 'min_row'

        return ''

    def highlight_rows(self):
        self.__table.tag_configure('max_row', background='magenta')
        self.__table.tag_configure('min_row', background='red')

    def unhighlight(self):
        self.__table.tag_configure('max_row', background='white')
        self.__table.tag_configure('min_row', background='white')

    def __init__(self, master):
        table = ttk.Treeview(master)
        table['columns'] = ()
        table.column('#0', width=0, stretch='no')
        table.heading("#0",text="", anchor='center')
        
        table.pack()

        self.__table = table