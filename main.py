import tkinter as tk
from tkinter import filedialog

filename = ""

def browseFiles():
    filename = filedialog.askopenfilename(initialdir="%USERNAME%",title = "Select a File",filetypes = (("CSV file.","*.csv*"),("all files","*.*")))
    lbl_filename.configure(text="File Opened: "+filename)

    print(csv2array(filename))


def csv2array(file):
    return file.read().splitlines()
    
root = tk.Tk()
root.geometry("800x600")
root.title("DB Creator")

tk.Label(root, text="DB Creator", font="Arial 20").place(x=50, y=10)

lbl_filename = tk.Label(root, text="DB Creator", font="Arial 12")
lbl_filename.place(x=110, y=77)
lbl_filename.configure(text="File: "+ filename)

tk.Button(root, text="Browse", command=browseFiles).place(x=50,y=75)
root.mainloop()