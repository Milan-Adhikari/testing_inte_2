from tkinter import *
import tkinter.font as font
from tkinter import messagebox

root = Tk()
root.title('Simple Calculator')
# root.geometry("281x354")
# root.resizable(width = False,height= False)
root.configure(bg = 'BLACK')
global temp1
global sign
global temp2

# image as background
# c = Canvas(root,height =354,width = 281)
# filename = PhotoImage(file = "C:\\Users\\adwin\\PycharmProjects\\dood.png")
# background_label = Label(root, image=filename)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)
#c.pack()
# fontsize
# myfont = font.Font(size =15)

# input field
e = Entry(root,width = 28,borderwidth =10)
e['font'] = font.Font(size =12)
e.grid(row = 0,column =0,columnspan = 5,padx = 10,pady =10)

# function
def click(number):
    temp = e.get()
    e.delete(0, END)
    e.insert(0,str(temp)+str(number))
def clearscreen():
    e.delete(0,END)
def addit():
    global sign
    sign = "+"
    global temp1
    temp1 = float(e.get())
    e.delete(0,END)
def subt():
    global sign
    global temp1
    sign = "-"
    temp1 = float(e.get())
    e.delete(0,END)
def divi():
    global sign
    global temp1
    sign = "/"
    temp1 = float(e.get())
    e.delete(0,END)
def multip():
    global sign
    global temp1
    sign = "*"
    temp1 = float(e.get())
    e.delete(0,END)
def equalsto():
    global sign
    global temp1
    temp2 = float(e.get())
    e.delete(0,END)
    if sign =="+":
        ans = temp1+temp2
        e.insert(0,ans)
    elif sign =="-":
        ans = temp1-temp2
        e.insert(0,ans)
    elif sign =="/":
        ans = temp1/temp2
        e.insert(0,ans)
    elif sign =="*":
        ans = temp1*temp2
        e.insert(0,ans)




# buttons
btn_1 = Button(root,text='1',height =1, width =4,command=lambda: click(1))
btn_1['font']=font.Font(size =15)
btn_1.grid(row= 4,column=0,padx=1,pady=1)
btn_2 = Button(root,text='2',height =1 , width =4,command = lambda: click(2))
btn_2['font']=font.Font(size =15)
btn_2.grid(row= 4,column=1,padx=1,pady=1)
btn_3 = Button(root,text='3',height =1 , width =4,command = lambda: click(3))
btn_3['font']=font.Font(size =15)
btn_3.grid(row= 4,column=2,padx=1,pady=1)
btn_4 = Button(root,text='4',height =1 , width =4,command = lambda: click(4))
btn_4['font']=font.Font(size =15)
btn_4.grid(row= 3,column=0,padx=1,pady=1)
btn_5 = Button(root,text='5',height =1 , width =4,command = lambda: click(5))
btn_5['font']=font.Font(size =15)
btn_5.grid(row= 3,column=1,padx=1,pady=1)
btn_6 = Button(root,text='6',height =1 , width =4,command = lambda: click(6))
btn_6['font']=font.Font(size =15)
btn_6.grid(row= 3,column=2,padx=1,pady=1)
btn_7 = Button(root,text='7',height =1 , width =4,command = lambda: click(7))
btn_7['font']=font.Font(size =15)
btn_7.grid(row= 2,column=0,padx=1,pady=1)
btn_8 = Button(root,text='8',height =1 , width =4,command = lambda: click(8))
btn_8['font']=font.Font(size =15)
btn_8.grid(row= 2,column=1,padx=1,pady=1)
btn_9 = Button(root,text='9',height =1 , width =4,command =lambda: click(9))
btn_9['font']=font.Font(size =15)
btn_9.grid(row= 2,column=2,padx=1,pady=1)
btn_10 = Button(root,bg='#7E878F',text='=',height =4 , width =4,padx=5,pady=5,command =equalsto)
btn_10['font']=font.Font(size =15)
btn_10.grid(row= 4,column=3,rowspan =2,padx=1,pady=1)
btn_11 = Button(root,bg='#7E878F',text='+',height =1 , width =4,padx=5,pady=5,command = addit)
btn_11['font']=font.Font(size =15)
btn_11.grid(row=1 ,column=0,padx=1,pady=1)
btn_12 = Button(root,bg='#7E878F',text='-',height =1 , width =4,padx=5,pady=5,command = subt)
btn_12['font']=font.Font(size =15)
btn_12.grid(row=1,column=1,padx=1,pady=1)
btn_13 = Button(root,bg='#7E878F',text='*',height =1 , width =4,padx=5,pady=5,command = multip)
btn_13['font']=font.Font(size =15)
btn_13.grid(row= 1,column=2,padx=1,pady=1)
btn_14 = Button(root,bg='#7E878F',text='/',height =1 , width =4,padx=5,pady=5,command = divi)
btn_14['font']=font.Font(size =15)
btn_14.grid(row= 1,column=3,padx=1,pady=1)
btn_15 = Button(root,bg='#7E878F',text='Clear',height =4 , width =4,padx=5,pady=5,command = clearscreen)
btn_15['font']=font.Font(size =14)
btn_15.grid(row=2 ,column=3,rowspan =2,padx=1,pady=1)
btn_16 = Button(root,text='0',height =1 , width =4,command = lambda: click(0))
btn_16['font']=font.Font(size =15)
btn_16.grid(row= 5,column=0,padx=1,pady=1)
btn_17 = Button(root,text='00',height =1 , width =4,command = lambda: click("00"))
btn_17['font']=font.Font(size =15)
btn_17.grid(row= 5,column=1,padx=1,pady=1)
btn_18 = Button(root,text='.',height =1 , width =4,command = lambda: click("."))
btn_18['font']=font.Font(size =15)
btn_18.grid(row= 5,column=2,padx=1,pady=1)



root.mainloop()

