from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile

def enter_data():
    l1.insert(END, inputbox.get())

def delete_data():
    candidate = l1.curselection()
    l1.delete(candidate)
    
def open_data():
    file = askopenfile(mode="r", title="File opened")
    if file is not None:
        l1.delete(0,END)
        #reading each line from the file
        items = file.readlines()
        for i in items:
            l1.insert(END,i)

def save_data():
    sfile = asksaveasfile(defaultextension="*.txt")
    if sfile is not None:
        for i in l1.get(0,END):
            print(i.strip(), file=sfile)

        l1.delete(0,END)






scr = Tk()
scr.geometry("300x300")

save_but = Button(scr, text="save", command=save_data)
save_but.pack(side="top")

inputbox = Entry(scr)
inputbox.pack(side="top")

add_but = Button(scr, text="Add", command=enter_data)
add_but.pack(side="top")

open_but = Button(scr, text="Open", command=open_data)
open_but.pack(side="right")

delete_but = Button(scr, text="Delete", command=delete_data)
delete_but.pack(side="left")


    

l1 = Listbox(scr, height=10, width=25, bg="lightgreen")

data = ["Apple", "Game", "Math", "Ball"]
for i in data:
    l1.insert(END, i)
l1.pack()



scr.mainloop()
