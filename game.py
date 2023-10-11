from tkinter import *
import random as r
from PIL import Image,ImageTk

def user_fun(event):
    if event == 1:
        e1.insert(END,"ROCK")
    if event == 2:
        e1.insert(END,"PAPER")
    if event == 3:
        e1.insert(END,"SCISSOR")

def comp_fun(event):
    l=["ROCK","PAPER","SCISSOR"]
    e2.insert(END,r.choice(l))

def sub_ans():
    val = e1.get()
    val2 = e2.get()

    if val == val2:
        e3.insert(END, "              TIE")
        e4.insert(END, "              TIE")
    elif val == "ROCK" and val2 == "SCISSOR":
        e3.insert(END, "              1")
        e4.insert(END, "              0")
    elif val == "PAPER" and val2 == "SCISSOR":
        e3.insert(END, "              0")
        e4.insert(END, "              1")
    elif val == "ROCK" and val2 == "PAPER":
        e3.insert(END, "              0")
        e4.insert(END, "              1")
    elif val == "SCISSOR" and val2 == "ROCK":
        e3.insert(END, "              0")
        e4.insert(END, "              1")
    elif val == "SCISSOR" and val2 == "PAPER":
        e3.insert(END, "              1")
        e4.insert(END, "              0")
    elif val == "PAPER" and val2 == "ROCK":
        e3.insert(END, "              1")
        e4.insert(END, "              0")

    val3 = e3.get()
    val4 = e4.get()

    if val3 == val4:
        e5.insert(END,"                  TIE :( ")
    if val3 > val4:
        e5.insert(END,"                  YOU :) ")
    elif val3 < val4:
        e5.insert(END,"               COMPUTER :( ")

def out():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

game = Tk()
game.title("ROCK,PAPER,SCISSOR GAME")
game.geometry("1024x640")
game.configure(background="pink",highlightbackground="black")
image=Image.open("C:\\Users\\LENOVO\\Downloads\\Java-Rock-Paper-Scissors-Game.jpeg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()

l= Label(game,text="ROCK , PAPER , SCISSOR  GAME",bg="red",font=("broadway",20,"bold"))
l.place(x=275,y=0)

l1 = Label(game,text="YOUR CHOICE",fg="Black",font=("bold",15))
l1.place(x=290,y=60)
e1 = Entry(game,font=("bold",15))
e1.place(x=520,y=60)

b1 = Button(game,text="ROCK",fg="white",bg="black",font=("bold",12),command=lambda :user_fun(1))
b1.place(x=390,y=120)
b2 = Button(game,text="PAPER",fg="white",bg="black",font=("bold",12),command=lambda:user_fun(2))
b2.place(x=490,y=120)
b3 = Button(game,text="SCISSOR",fg="white",bg="black",font=("bold",12),command=lambda:user_fun(3))
b3.place(x=590,y=120)

l2 = Label(game,text="COMPUTER CHOICE",fg="Black",font=("bold",15))
l2.place(x=290,y=230)
e2 = Entry(game,font=("bold",15))
e2.place(x=520,y=230)
e2.bind('<FocusIn>',comp_fun)

b4 = Button(game,text="SUBMIT",fg="blue",bg="yellow",font=("broadway",17,"bold"),command=lambda:sub_ans())
b4.place(x=440,y=310)

l3 = Label(game,text="Your Score",fg="White",bg="black",font=("bold",15))
l3.place(x=280,y=380)
e3 = Entry(game,fg="red",font=("bold",15))
e3.place(x=220,y=410)

l4 = Label(game,text="Computer Score",fg="White",bg="black",font=("bold",15))
l4.place(x=600,y=380)
e4 = Entry(game,fg="red",font=("bold",15))
e4.place(x=560,y=410)

l5 = Label(game,text="WINNER",fg="black",bg="Aqua",font=("bold",20))
l5.place(x=470,y=510)
e5 = Entry(game,font=("broadway",20,"bold"))
e5.place(x=340,y=562)

b5 = Button(game,text="PLAY AGAIN",fg="white",bg="black",font=("bold",13),command=lambda:out())
b5.place(x=900,y=550)



game.mainloop()
