from tkinter import *

class MyButton:
    def __init__(self,rootone):
        frame = Frame (rootone)
        frame.pack()

        self.printButton = Button(frame,text = "Click Here",bg ="Green",fg = "white",command = self.printmessage)
        self.printButton.pack()
        self.quitButton = Button(frame,text = "Exit",bg = "Red",command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printmessage(self):
        print("Button Clicked")

root = Tk()
b = MyButton(root)

root.mainloop()