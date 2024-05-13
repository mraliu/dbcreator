import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Check
def createstructure(data):
    tablestructure = [False for _ in range(len(data[0].split(",")))]
    for d in data:
        headings = d.split(",")
        for id, field in enumerate(headings):
            tablestructure[id] = field.isnumeric()
    tablestructure = ["INTEGER" if dt == True else "TEXT" for dt in tablestructure ]
    return tablestructure

# Get filename
def getfilename(filenamedir):
    return filenamedir[filenamedir.rfind("/")+1:]

# Get name of file
def getnameoffile(filename):
    return filename[:filename.rfind(".")]

# SQL Create Statement
def createtable():
    tablestructure = createstructure(thedata)
    # print(tablestructure)
    # print("Number of fields:", len(csvheadings), filenamedir)
    filen = getnameoffile(filename)
    sql_newtable = f"CREATE TABLE IF NOT EXISTS {filen} ("
    for idx, field in enumerate(csvheadings):
        sql_newtable+="'" + field + "' " + tablestructure[idx] + ", "
    sql_newtable = sql_newtable[:-2] + ")"

    print(sql_newtable)
    return sql_newtable


# GUI for window
def browseFiles():  # Part of the browse button
    global csvheadings, thedata, filenamedir, filename
    filenamedir = filedialog.askopenfilename(initialdir = "%USERNAME%", title = "Select a File", filetypes = (("CSV file." ,"*.csv*"), ("All files" ,"*.*")))
    lbl_filename.configure(text="File opened: "+filenamedir)
    filename = getfilename(filenamedir)
    csvheadings = tuple(csv2array(filenamedir)[0].split(","))
    thedata = csv2array(filenamedir)[1:21]

    # Show treeview
    dataview = displaytable(csvheadings, thedata)
    dataview.place(x=50,y=125, width=700)

    # Place scrollbars
    scrollbarv.place(x=759, y=125, height=250) # Use place to put beside treeview
    scrollbarh.place(x=50, y=375, width=700) # Use place to put beside treeview
    
    # Config scrollbars action to the treeview
    scrollbarv.config(command = dataview.yview)
    scrollbarh.config(command = dataview.xview)

    lbl_status.configure(text="Previewing 20 records.")
    btn_dbcreate = tk.Button(root, text="Create", command=createtable)
    btn_dbcreate.place(x=50,y=90)

def csv2array(file: str):
    return open(file, encoding="utf8").read().splitlines()

def displaytable(fielding, thedata):
    treeview = ttk.Treeview(columns=(fielding), yscrollcommand = scrollbarv.set, xscrollcommand=scrollbarh.set)
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

filenamedir = ""
filename = ""
csvheadings = () # Need to construct table in db
thedata = [] # Need to insert into db

# MAIN PROGRAM    
root = tk.Tk()
root.geometry("800x400")
root.resizable(False,False)
root.title("CSV to DBlite3")

# Scrollbars
scrollbarv = tk.Scrollbar(root, orient="vertical") # Scroll bar for treeview
scrollbarh = tk.Scrollbar(root, orient="horizontal") # Scroll bar for treeview

# Label title
tk.Label(root, text="CSV to DBlite3", font="Arial 20").place(x=50, y=10)

# Label for browse
lbl_filename = tk.Label(root, text="DB Creator", font="Arial 10")
lbl_filename.place(x=110, y=62)
lbl_filename.configure(text="File: "+ filenamedir)

# Button for browse
tk.Button(root, text="Browse", command=browseFiles).place(x=50,y=60)

# Label for status
lbl_status = tk.Label(root, text="", font="Arial 10")
lbl_status.place(x=50, y=355)

root.mainloop()