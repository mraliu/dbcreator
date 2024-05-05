import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# MAIN PROGRAM    
root = tk.Tk()
root.geometry("800x600")
root.title("DB Creator")

def show_info():
    # Get the text of the item whose Id is stored in `my_iid`.
    text = treeview.item("I002", option="text")
    # Display it within a message box.
    messagebox.showinfo(title="Item Info", message=text)

tk.Label(root, text="Tree View", font="Arial 20").place(x=10, y=10)
treeview = ttk.Treeview()

item = treeview.insert("", tk.END, text="Item 1")
treeview.insert(item, tk.END, text="Subitem 1")
treeview.insert(item, tk.END, text="Subitem 2")

treeview.place(x=10, y=50)

button = ttk.Button(text="Show info", command=show_info)
button.place(x=250, y=50)


root.mainloop()