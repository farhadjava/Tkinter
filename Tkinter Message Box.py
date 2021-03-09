from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title","This is awesome")

response = tkinter.messagebox.askquestion("Question 1","Do you like Coffee")


if response == 'yes':
    print("Here is a Coffee for You..!")
else:
    print('OK',"Thank You")


root.mainloop()
