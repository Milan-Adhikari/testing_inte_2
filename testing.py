import tkinter
from turtle import RawTurtle,TurtleScreen,Canvas
from tkinter import *
import random
import tkinter.font as font
# main window
root = tkinter.Tk()
root.title('Root Window')
root.configure(bg ='black')
root.geometry('300x400')
#welcome text
my_font = font.Font(size = 15)
welcome = Label(root,font = my_font,  text = 'Welcome to Pong Valley').place(relx = 0.5,rely =0.3, anchor = 'center')
# player name
text1 = Label(root,  text = 'Enter Name of Player 1').place(relx = 0,rely =0.45)
text2 = Label(root,  text = 'Enter Name of Player 2').place(relx = 0.57,rely =0.45)

#make input boxes
pla1 = Entry(root,width = 15,borderwidth =5)
pla1.place(relx=0.04, rely = 0.55)
pla2 = Entry(root,width = 15,borderwidth =5)
pla2.place(relx=0.61, rely = 0.55)
name_1 = pla1.get()
name_2 = pla2.get()

#next button and function
def next(a,b):
    new_win = Toplevel()
    root.withdraw()
    new_win.configure(bg = 'black')
    new_win.geometry('300x400')
    tex = Label(new_win, text = 'Are you ready '+str(a)+' and '+str(b) + '?')
    tex.place(relx = 0.25,rely = 0.3)
    yes_btn = Button(new_win, text='YES')
    yes_btn.place(relx=0.43, rely=0.45)
    exit_btn = Button(new_win, text='EXIT',command = root.destroy)
    exit_btn.place(relx=0.43, rely=0.6)

next_btn = Button(root,text = 'NEXT',command = lambda: next(pla1.get(),pla2.get()))
next_btn.place(relx = 0.43,rely = 0.7)

root.mainloop()