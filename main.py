import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk

# New Features

def browseFiles():  # Part of the browse button
    global myheadings, lbl_status, lbl_filename
    filename = filedialog.askopenfilename(initialdir = "%USERNAME%", title = "Select a File", filetypes = (("CSV file." ,"*.csv*"),("All files" ,"*.*")))
    lbl_filename.configure(text="File opened: "+filename)
    myheadings = tuple(csv2array(filename)[0].split(","))
    thedata = csv2array(filename)[1:21]
    displaytable(myheadings, thedata).place(x=50,y=125, width=700)
    lbl_status.configure(text="Previewing 20 records.")
    btn_dbcreate = tk.Button(root, text="Create")
    btn_dbcreate.place(x=50,y=90)

def csv2array(file: str):
    return open(file, encoding="utf8").read().splitlines()

def displaytable(fielding, thedata):
    treeview = ttk.Treeview(columns=(fielding))

    # Unique column
    treeview.column('#0', anchor=tk.CENTER, stretch=tk.YES, width=35)
    treeview.heading('#0', text="#")

    # The headings
    for i in range(0, len(fielding)):
        treeview.column(fielding[i], anchor=tk.CENTER, stretch=tk.YES, width=80)
        treeview.heading(fielding[i], text=fielding[i])

    # The data
    for row, data in enumerate(thedata):
        rowinfo = data.split(",")
        treeview.insert("", tk.END, text=row+1, values=tuple(rowinfo))
    return treeview

filename = ""
myheadings = ()

# MAIN PROGRAM    
root = tk.Tk()
root.geometry("800x400")
root.resizable(False,False)
root.title("DB Creator")

tk.Label(root, text="DB Creator", font="Arial 20").place(x=50, y=10)

lbl_filename = tk.Label(root, text="DB Creator", font="Arial 10")
lbl_filename.place(x=110, y=62)
lbl_filename.configure(text="File: "+ filename)

tk.Button(root, text="Browse", command=browseFiles).place(x=50,y=60)

lbl_status = tk.Label(root, text="", font="Arial 10")
lbl_status.place(x=50, y=355)

root.mainloop()