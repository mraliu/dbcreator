import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# MAIN PROGRAM    
root = tk.Tk()
root.geometry("800x600")
root.title("DB Creator")

tk.Label(root, text="Tree View", font="Arial 20").place(x=10, y=10)

def displaytable():
    treeview = ttk.Treeview(columns=("size", "lastmod"))
    treeview.heading("#0", text="File")
    treeview.heading("size", text="Size")
    treeview.heading("lastmod", text="Last modification")
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))
    treeview.insert("", tk.END, text="README.txt", values=("850 bytes", "18:30"))

    return treeview

displaytable().place(x=10, y=50)




root.mainloop()