from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look I Clicked a Button!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", command=myClick, fg="red", bg="#000000")
myButton.pack()

root.mainloop()