from tkinter import *

def function1():
    print('Menu item clicked')

root = Tk()

mymenu = Menu(root)
root.config (menu=mymenu)
submenu = Menu(mymenu)

mymenu.add_cascade(label="Fill",menu = submenu)

submenu.add_command(label="project", command=function1)
submenu.add_command(label="save",command=function1)

submenu.add_separator()
submenu.add_command(label="Exit",command=function1)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo",command=function1)

toolbar = Frame(root,bg= "Red")
insertbutton = Button(toolbar,text = "Insert File",command = function1)
insertbutton.pack(side = LEFT,padx = 2, pady = 3)

printbutton = Button(toolbar,text = "print",command = function1)
printbutton.pack(side = LEFT,padx = 2, pady = 3)

toolbar.pack(side = TOP,fill = X)

status = Label(root,text = "status",bd = 1,relief = SUNKEN,anchor = W)
status.pack(side = BOTTOM,fill = X)

root.mainloop()