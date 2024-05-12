import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calltable():
    # treeview = ttk.Treeview(columns=("size", "lastmod"), yscrollcommand = scrollbarv.set, xscrollcommand = scrollbarh.set)
    treeview = ttk.Treeview(columns=("size", "lastmod","size", "lastmod"), yscrollcommand = scrollbarv.set, xscrollcommand=scrollbarh.set)

    treeview.heading("#0", text="File")
    treeview.heading("size", text="Size")
    treeview.heading("lastmod", text="Last modification")
    treeview.heading("size", text="Size")
    treeview.heading("lastmod", text="Last modification")

    for i in range(100):
        treeview.insert("", tk.END, text=i, values=("850 bytes", "18:30"))

    treeview.place(x=10, y=50, width=700, height=200)
    scrollbarv.place(x=710, y=50, height=200)
    scrollbarv.config(command = treeview.yview)

    scrollbarh.place(x=10, y=250, width=700)
    scrollbarh.config(command = treeview.xview)


# MAIN PROGRAM    
root = tk.Tk()
root.geometry("800x600")
root.title("DB Creator")

tk.Label(root, text="Tree View", font="Arial 20").place(x=10, y=10)

scrollbarv = tk.Scrollbar(root, orient='vertical')
scrollbarh = tk.Scrollbar(root, orient='horizontal')

calltable()





root.mainloop()