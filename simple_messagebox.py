from tkinter import *
from tkinter import messagebox

root = Tk()

def popup():
    messagebox.showinfo("Error","This is the message")

button1 = Button(root,text = " Dont press",command = popup).pack()
root.mainloop()