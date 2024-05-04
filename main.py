import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

filename = ""
myheadings = ()

def browseFiles():
    global myheadings
    filename = filedialog.askopenfilename(initialdir="%USERNAME%",title = "Select a File",filetypes = (("CSV file.","*.csv*"),("all files","*.*")))
    lbl_filename.configure(text="File Opened: "+filename)
    myheadings = tuple(csv2array(filename)[0].split(","))
    thedata = csv2array(filename)[1:]
    displaytable(myheadings, thedata).place(x=50,y=125)

def csv2array(file: str):
    return open(file, encoding="utf8").read().splitlines()

def displaytable(fielding, thedata):
    treeview = ttk.Treeview(columns=(fielding))

    # Unique column
    treeview.column('#0',anchor=tk.CENTER, stretch=tk.YES, width=100)
    treeview.heading('#0', text="#")

    # The headings
    for field in fielding:
        treeview.column(field,anchor=tk.CENTER, stretch=tk.YES, width=100)
        treeview.heading(field, text=field)

    # The data
    for data in thedata:
        rowinfo = data.split(",")
        treeview.insert("", tk.END, text="", values=tuple(rowinfo))

    return treeview


# MAIN PROGRAM    
root = tk.Tk()
root.geometry("800x400")
root.title("DB Creator")

tk.Label(root, text="DB Creator", font="Arial 20").place(x=50, y=10)

lbl_filename = tk.Label(root, text="DB Creator", font="Arial 10")
lbl_filename.place(x=110, y=77)
lbl_filename.configure(text="File: "+ filename)

tk.Button(root, text="Browse", command=browseFiles).place(x=50,y=75)

root.mainloop()