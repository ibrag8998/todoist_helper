import tkinter as tk
from tkinter import ttk


class UI:

    def __init__(self):
        self.root = tk.Tk()
        self.center_root()
        self.root.bind('<Control-Key-w>', self.close)
        self.root.bind('<Return>', self.save)

        self.mainframe = ttk.Frame(self.root, padding='20 20 20 20')
        self.mainframe.grid(row=0, column=0)

        self.task = tk.StringVar()
        self.close_window = False

    def quick_add(self):
        legend = ttk.Label(self.mainframe, text='Add Task')
        legend.grid(row=0, column=0)

        task_entry = ttk.Entry(self.mainframe, textvariable=self.task)
        task_entry.grid(row=1, column=0)
        task_entry.focus()

        btn = ttk.Button(self.mainframe, text='Add Task', command=self.save)
        btn.grid(row=2, column=0)

        self.grid_configure()
    
    def grid_configure(self):
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=10, pady=5)

    def center_root(self):
        pos_x = int(self.root.winfo_screenwidth()/2 - self.root.winfo_reqwidth()/2)
        pos_y = int(self.root.winfo_screenheight()/2 - self.root.winfo_reqheight()/2)
        self.root.geometry("+{}+{}".format(pos_x, pos_y))

    def close(self, *args):
        self.close_window = True
        self.task.set('')
        self.root.destroy()
    
    def save(self, *args):
        self.close_window = False
        self.root.destroy()

    def mainloop(self):
        self.root.mainloop()
