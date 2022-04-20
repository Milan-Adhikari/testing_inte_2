from turtle import RawTurtle,TurtleScreen,Canvas
from tkinter import *
import tkinter
import random
import tkinter.font as font
import time

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

#exit_win
def exit(newer_win,c,d,score_a,score_b):
    newer_win.destroy()
    last_win = Toplevel()
    last_win.geometry('300x400')
    last_win.configure(bg = 'black')
    last_win.title("Result")
    if score_a>score_b:
        label = Label(last_win,text = ' Congrats {}, You won.'.format(c))
        label.place(relx=0.5,rely=0.5,anchor= 'center')
    elif score_b>score_a:
        label = Label(last_win, text=' Congrats {}, You won'.format(d))
        label.place(relx=0.5, rely=0.5,anchor = 'center')
    else:
        label = Label(last_win, text= ' It was a draw')
        label.place(relx=0.5, rely=0.5,anchor = 'center')
    btn2 = Button(last_win,text = 'End Game',command = root.destroy)
    btn2.place(relx=0.5,rely=0.8,anchor = 'center')


#turtle_win windows
def turtle_win(new_win,c,d):
     global turtle
     new_win.destroy()
     newer_win = Toplevel()
     newer_win.title('Pong')
     newer_win.configure(bg='white')
     newer_win.geometry('300x470')
     delay = 0.1

     # canvas
     canvas = Canvas(newer_win)
     canvas.place(relx = 0.5,rely=0.5,anchor='center')
     canvas.configure(width = 300, height = 400)
     win = TurtleScreen(canvas)
     win.tracer(0)

     #ball
     ball = RawTurtle(canvas)
     ball.penup()
     ball.goto(x=0, y=0)
     ball.shape('circle')
     ball.up()
     ball.speed(0)
     ball.dx = 3
     ball.dy = 4

     #pad_a
     pad_a = RawTurtle(canvas)
     pad_a.penup()
     pad_a.goto(x=-140, y=0)
     pad_a.shape('square')
     pad_a.shapesize(stretch_wid=5,stretch_len=1)
     pad_a.up()
     pad_a.speed(0)

     #pad_b
     pad_b = RawTurtle(canvas)
     pad_b.penup()
     pad_b.goto(x=140, y=0)
     pad_b.shape('square')
     pad_b.shapesize(stretch_wid=5, stretch_len=1)
     pad_b.up()
     pad_b.speed(0)

     # score
     score_a = 0
     score_b = 0
     score = RawTurtle(canvas)
     score.penup()
     score.hideturtle()
     score.speed(0)
     score.goto(0,180)
     score.write("{}: {}     {}: {}".format(c,score_a,d, score_b), align="center", font=("arial", 15))

     #Functions
     def a_up():
         y = pad_a.ycor()
         pad_a.sety(y+20)

     def a_down():
         y = pad_a.ycor()
         pad_a.sety(y - 20)

     def b_up():
         y = pad_b.ycor()
         pad_b.sety(y + 20)

     def b_down():
         y = pad_b.ycor()
         pad_b.sety(y-20)

     def movement():
         ball.sety(ball.ycor() + ball.dy)
         ball.setx(ball.xcor() + ball.dx)

     #Keyboard
     win.listen()
     win.onkeypress(a_up,'w')
     win.onkeypress(a_down, 's')
     win.onkeypress(b_up, 'Up')
     win.onkeypress(b_down, 'Down')

     btn = Button(newer_win, text='Finish', command=lambda: exit(newer_win, c, d, score_a, score_b))
     btn.place(relx=0.45, rely=0.94)

     while (score_a<100 and score_b<100):

         newer_win.update()

         movement()

         # boundary
         if ball.ycor() > 190:
             ball.sety(190)
             ball.dy *= -1
         if ball.ycor() < -190:
             ball.sety(-190)
             ball.dy *= -1
         if ball.xcor() > 150:
             ball.goto(0, 0)
             time.sleep(delay)
             score_a += 10
             score.clear()
             score.write("{}: {}     {}: {}".format(c,score_a,d, score_b), align="center", font=("arial", 15))
         if ball.xcor() < -150:
             ball.goto(0, 0)
             time.sleep(delay)
             score_b += 10
             score.clear()
             score.write("{}: {}     {}: {}".format(c,score_a,d, score_b), align="center", font=("arial", 15))
         if ball.xcor() > 120 and (ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50):
             ball.setx(120)
             ball.dx *= -1
         if ball.xcor() < -120 and (ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50):
             ball.setx(-120)
             ball.dx *= -1
     newer_win.mainloop()

#next button and function
def next(a,b):
    new_win = Toplevel()
    root.withdraw()
    new_win.configure(bg = 'black')
    new_win.geometry('300x400')
    tex = Label(new_win, text = 'Are you ready '+str(a)+' and '+str(b) + '?')
    tex.place(relx = 0.25,rely = 0.3)
    yes_btn = Button(new_win, text='YES',command = lambda : turtle_win(new_win,a,b))
    yes_btn.place(relx=0.43, rely=0.45)
    exit_btn = Button(new_win, text='EXIT',command = root.destroy)
    exit_btn.place(relx=0.43, rely=0.6)

next_btn = Button(root,text = 'NEXT',command = lambda: next(pla1.get(),pla2.get()))
next_btn.place(relx = 0.43,rely = 0.7)

root.mainloop()