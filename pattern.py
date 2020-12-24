import tkinter as tk
from tkinter import *

gui = tk.Tk()
gui.title('PATTERN ')
gui.geometry('500x500')
gui.config(bg='blue')
text_Input = StringVar()

def p1():
    l1 = Label(gui, text='*', bg='black', fg='white').place(x=150,y=130)
    l2 = Label(gui, text='* *', bg='black', fg='white').place(x=150,y=150)
    l3 = Label(gui, text='* * *', bg='black', fg='white').place(x=150,y=170)
    l4 = Label(gui, text='* * * *', bg='black', fg='white').place(x=150,y=190)
    l5 = Label(gui, text='* * * * *', bg='black', fg='white').place(x=150,y=210)

def p2():
    l1 = Label(gui, text='*', bg='black', fg='white').place(x=150,y=310)
    l2 = Label(gui, text='* *', bg='black', fg='white').place(x=150,y=290)
    l3 = Label(gui, text='* * *', bg='black', fg='white').place(x=150,y=270)
    l4 = Label(gui, text='* * * *', bg='black', fg='white').place(x=150,y=250)
    l5 = Label(gui, text='* * * * *', bg='black', fg='white').place(x=150,y=230)

def p3():
    l1 = Label(gui, text='*', bg='black', fg='white').place(x=150,y=330)
    l2 = Label(gui, text='* *', bg='black', fg='white').place(x=150,y=350)
    l3 = Label(gui, text='* * *', bg='black', fg='white').place(x=150,y=370)
    l4 = Label(gui, text='* * * *', bg='black', fg='white').place(x=150,y=390)
    l5 = Label(gui, text='* * * * *', bg='black', fg='white').place(x=150,y=410)

def p4():
    l1 = Label(gui, text='*', bg='black', fg='white').place(x=150,y=330)
    l2 = Label(gui, text='* *', bg='black', fg='white').place(x=150,y=350)
    l3 = Label(gui, text='* * *', bg='black', fg='white').place(x=150,y=370)
    l4 = Label(gui, text='* * * *', bg='black', fg='white').place(x=150,y=390)
    l5 = Label(gui, text='* * * * *', bg='black', fg='white').place(x=150,y=410)

       
b1 = Button(gui, text='PATTERN 1', command=p1).place(x=100,y=40)
b2 = Button(gui, text='PATTERN 2', command=p2).place(x=200,y=40)
b3 = Button(gui, text='PATTERN 3', command=p3).place(x=300,y=40)
b4 = Button(gui, text='PATTERN 4', command=p4).place(x=400,y=40)
gui.mainloop()
