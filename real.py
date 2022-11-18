from tkinter import ttk
import tkinter as tk
import sqlite3 as sq

window = tk.Tk()
window.title("Main menu")
#window.config(bg="grey")
window.geometry("500x500")
conn = sq.connect("full.db")
c = conn.cursor()
titleentry = tk.StringVar() #for creating table
searchname = tk.StringVar() # for searching one table
textentry=tk.StringVar() #for deleting table
everydata = tk.StringVar() #for entering all data while inserting
allcol = tk.StringVar() #for creating table column


tname = tk.StringVar() #for editing table

input1 = ["'300m'", "'400m'"]

#c.execute("create table if not exists a(" + ('%s text,' * len(input1)) + ")\"" % (input1[0], input1[1]))
#c.execute("insert into '17/11' values('d', '11.00', '22.00', '33.00')")
#c.execute("create table if not exists '17/11'(name text, '1' text, '2' text)")
#c.execute("alter table '17/11' add '3' text")

#for j in input1:
#    c.execute("alter table '18/11' add " + j + " text")


#for widgets in window.winfo_children():
#    widgets.destroy()


    

#edit select
def editselect():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    createbut = tk.Button(fr, text="create new", command=createtable)
    editbut = tk.Button(fr, text="edit existing", command=editexisting)
    menubut=tk.Button(text="Main menu", command=mainmenu)

    menubut.pack(side="top", anchor="nw")

    createbut.pack()
    editbut.pack()
    fr.place(relx=0.5, rely=0.5, anchor="center")



#create table
def createtable():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    instrlabel = tk.Label(fr, text="Please enter the title of the table")
    title = tk.Entry(fr, textvariable=titleentry)
    backbut=tk.Button(text="Main menu", command=mainmenu)
    enterbut = tk.Button(text="Enter", command=createcol)


    instrlabel.pack()
    title.pack()
    backbut.pack(side="top", anchor="nw")
    enterbut.pack(side="bottom", anchor="se")
    fr.place(relx=0.5, rely=0.5, anchor="center")

#creating columns
def createcol():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    label = tk.Label(fr, text="Please enter all columns")
    colentry = tk.Entry(fr, textvariable=allcol)
    firmbut = tk.Button(fr, text="confirm", command=processcreation)
    menubut=tk.Button(text="Main menu", command=mainmenu)

    menubut.pack(side="top", anchor="nw")

    label.pack()
    colentry.pack()
    firmbut.pack()
    fr.place(relx=0.5, rely=0.5, anchor="center")

#process creating table
def processcreation():
    c.execute("create table if not exists " + titleentry.get() + "(name text)")

    for i in allcol.get().split(" "):
        c.execute("alter table " + titleentry.get() + " add " + i + " text")
        #c.execute("alter table '18/11' add " + j + " text")
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    label = tk.Label(fr, text="Table successfully created")
    backbut = tk.Button(fr, text="Back to main menu", command=mainmenu)
    label.pack()
    backbut.pack()
    fr.place(relx=0.5, rely=0.5, anchor="center")

#edit existing
def editexisting():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    tablename = tk.Entry(fr, textvariable=tname)
    label = tk.Label(fr, text="Please the name of the table")
    menubut=tk.Button(text="Main menu", command=mainmenu)

    menubut.pack(side="top", anchor="nw")
    firmbut = tk.Button(fr, text="confirm", command=entercol)
    label.pack()
    tablename.pack()
    firmbut.pack(side="bottom", anchor="se")
    fr.place(relx=0.5, rely=0.5, anchor="center")

#enter data for column
def entercol():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)

    label = tk.Label(fr, text="Please enter all data at once")
    alldata = tk.Entry(fr, textvariable=everydata)
    firmbut = tk.Button(fr, text="confirm", command=processdata)

    label.pack()
    alldata.pack()
    firmbut.pack()
    fr.place(relx=0.5, rely=0.5, anchor="center")

#process all entered data
def processdata():
    c.execute("select * from " + tname.get())
    one = c.fetchall()
    colname = c.execute("select * from " + tname.get()).description

    c.execute("insert into " + tname.get() + " values (" + ('?,' * len(colname))[:-1] + ")", everydata.get().split(" "))
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    label = tk.Label(fr, text="Success")
    returnbut = tk.Button(fr, text="Back to main menu", command=mainmenu)
    label.pack()
    returnbut.pack()
    fr.place(relx=0.5, rely=0.5, anchor="center")

#delete table
def deltable():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    label = tk.Label(fr, text="Please enter the name of the table that you want to delete")
    entry = tk.Entry(fr, textvariable= textentry)
    firmbut = tk.Button(text="Confirm", command=delsuccess)
    menubut=tk.Button(text="Main menu", command=mainmenu)

    firmbut.pack(side="bottom", anchor="se")
    label.pack()
    entry.pack()
    menubut.pack(side="top", anchor="nw")
    fr.place(relx=0.5, rely=0.5, anchor="center")

def delsuccess():
    for widgets in window.winfo_children():
        widgets.destroy()

    fr = tk.Frame(window)
    c.execute("select name from sqlite_master")
    before = c.fetchall()

    c.execute("drop table if exists " + textentry.get())

    c.execute("select name from sqlite_master")
    after = c.fetchall()
    if after == before:
        faillabel = tk.Label(fr, text="Table name do not exist")
        faillabel.pack()
    else:
        label = tk.Label(fr, text="Success")
        label.pack()
        conn.commit()

    backbut = tk.Button(fr, text="Back to Main Menu", command=mainmenu)
    backbut.pack()
    fr.place(relx=0.5, rely=0.5, anchor="center")








#show menu
def showmenu():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)
    showallbut = tk.Button(fr, text="list all",height=2, width=6, command=listall)
    showonebut = tk.Button(fr, text="search one",height=2, width=6, command=searchtable)
    menubut=tk.Button(text="Main menu", command=mainmenu)

    menubut.pack(side="top", anchor="nw")
    showallbut.pack(side="left")
    showonebut.pack(side="right")
    fr.place(relx=0.5, rely=0.5, anchor='center')

#enter name of the table
def searchtable():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)

    label = tk.Label(fr, text="Please enter the name of the table")
    firmbut = tk.Button(text="Confirm", command=showonetable)
    entry = tk.Entry(fr, textvariable=searchname)
    menubut=tk.Button(text="Main menu", command=mainmenu)

    menubut.pack(side="top", anchor="nw")
    label.pack()
    entry.pack()
    firmbut.pack(side="bottom", anchor='se')
    fr.place(relx=0.5, rely=0.5, anchor='center')


#show the table
def showonetable():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)


    c.execute("select * from " + searchname.get())
    one = c.fetchall()
    colname = c.execute("select * from " + searchname.get()).description

    label = tk.Label(fr, text=searchname.get())
    tree = ttk.Treeview(fr, selectmode="browse", show="headings")

    tree["column"] = colname
    for i in range(len(colname)):
        tree.column(i, anchor="center", width=int(500/(len(colname)+1)))
        tree.heading(i, text=colname[i][0])

    if len(one) > 0:
        for x in one:
            tree.insert("", tk.END, values=x)


    label.pack()
    tree.pack(fill="x", expand=True)

    menubut=tk.Button(text="Main menu", command=mainmenu)
    menubut.pack(side="top", anchor="nw")
    #fr.place(relx=0.5, rely=0.5, anchor='center')
    fr.pack(fill='x', expand=True)

#show all table
def listall():
    for widgets in window.winfo_children():
        widgets.destroy()
    fr = tk.Frame(window)

    c.execute("select name from sqlite_master")
    one = c.fetchall()

    tree = ttk.Treeview(fr, selectmode="browse", show="headings")

    tree["column"] = ("1")
    
    for x in one:
        tree.insert("", tk.END, values=x)
    tree.heading('#1', text="List of all table")    
    
    tree.pack()
    menubut=tk.Button(text="Main menu", command=mainmenu)

    menubut.pack(side="top", anchor="nw")
    fr.place(relx=0.5, rely=0.5, anchor="center")







#Main menu
def mainmenu():
    for widgets in window.winfo_children():
        widgets.destroy()
    fra = tk.Frame(window)

    label = tk.Label(fra, text="Welcome to the system", font=("Arial", 20))
    addbut = tk.Button(fra, text="Edit", height=2, width=6, command=editselect)
    showbut = tk.Button(fra, text="Show table", height=2, width=6, command=showmenu)
    delbut = tk.Button(fra, text="Delete", height=2, width=6, command=deltable)

    label.pack()
    addbut.pack(side="left")
    showbut.pack(side="right")
    delbut.pack()

    fra.place(relx=0.5, rely=0.5, anchor="center")


mainmenu()
window.mainloop()