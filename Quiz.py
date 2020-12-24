e3=""
e5=""
e7=""

import tkinter as tk
from tkinter import *
from tkinter import messagebox
import time as tm
second=0

ammara = tk.Tk()
ammara.title('QUIZ')
ammara.configure(bg='#BB8FCE')
#ammara.geometry('800x200')

def ammuu():
    global second
    if (second>20):
        messagebox.showwarning("YOU LOSE","Your time is up")
        ammara.destroy()
    else:
        timer=Label(ammara,text=str(second),font=('arial',20,'bold'))
        second+=1
        timer.grid(row=8,column=1)
        timer.after(1000,ammuu)

def check():
    global e3
    global e5
    global e7
    if e3.get()=='input':
        a = 'correct'
        print(a)
        f = open('quiz.txt','w')
        f.writelines(a)
        f.close()
    else:
        a = 'incorrect'
        print(a)
        print('incorrect')
    
    if e5.get()=='input':
        b = 'correct'
        print(b)
        f = open('quiz.txt','w')
        f.writelines(b)
        f.close()
    else:
        b = 'incorrect'
        print(b)
        print('incorrect')
    if e7.get()=='output':
        c = 'correct'
        print(c)
        f = open('quiz.txt','w')
        f.writelines(b)
        f.close()
    else:
        c = 'incorrect'
        print(c)
        print('incorrect')


ammuu()



lo = Label(ammara, text='QUIZ SYSTEM', font=('arial',20,'bold underline')).grid(row=0,column=1,pady=10)
l0 = Label(ammara, text='TIME LEFT:', font=('arial',20,'bold')).grid(row=8,column=0,padx=90,pady=15)
l1 = Label(ammara, text=' STUDENT NAME:', font=('arial',15,'bold')).grid(row=1,column=0,padx=10,sticky='w',pady=10)
l2 = Label(ammara, text='QUESTION 1:', font=('arial',15,'bold')).grid(row=2,column=0,padx=10,sticky='w',pady=10)
l3 = Label(ammara, text='ANSWERS:', font=('arial',15,'bold')).grid(row=3,column=0,padx=10,sticky='w',pady=10)
l4 = Label(ammara, text='QUESTION 2:', font=('arial',15,'bold')).grid(row=4,column=0,padx=10,sticky='w',pady=10)
l5 = Label(ammara, text='ANSWERS:', font=('arial',15,'bold')).grid(row=5,column=0,padx=10,sticky='w',pady=10)
l6 = Label(ammara, text='QUESTION 3:', font=('arial',15,'bold')).grid(row=6,column=0,padx=10,sticky='w',pady=10)
l7 = Label(ammara, text='ANSWERS:', font=('arial',15,'bold')).grid(row=7,column=0,padx=10,sticky='w',pady=10)

e1 = Entry(ammara, width=100, bd=6)
e1.grid(row=1,column=1,padx=3,pady=10)
la = Label(ammara,text='Is keyboard an Input Device or Output Device? ', font=('arial',15,'bold'), width=100, bd=6).grid(row=2,column=1,padx=3,pady=10, sticky='w')
e3 = Entry(ammara, width=100, bd=6)
e3.grid(row=3,column=1,padx=3,pady=10)
lb = Label(ammara,text='Is Mouse an Input Device or Output Device? ', font=('arial',15,'bold'), width=100, bd=6).grid(row=4,column=1,padx=3,pady=10, sticky='w')
e5 = Entry(ammara, width=100, bd=6)
e5.grid(row=5,column=1,padx=3,pady=20)
lc = Label(ammara,text='Is Monitor an Input Device or Output Device? ', font=('arial',15,'bold'), width=100, bd=6).grid(row=6,column=1,padx=3,pady=10, sticky='w')
e7 = Entry(ammara, width=100, bd=6)
e7.grid(row=7,column=1,padx=3,pady=10)

b1 = Button(ammara, text='SUBMIT', command=check, width=20).grid(row=9,column=1,sticky='w',padx=10,pady=10)

ammara.mainloop()
