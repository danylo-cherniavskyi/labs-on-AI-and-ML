from tkinter import ttk

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

    def __init__(self, master):
        table = ttk.Treeview(master)
        table['columns'] = ()
        table.column('#0', width=0, stretch='no')
        table.heading("#0",text="", anchor='center')
        
        table.pack()

        self.__table = table