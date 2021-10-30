#import mysql.connector
from tkinter import *
from tkinter import messagebox
import pyttsx3
#db=mysql.connector.connect(host='localhost',user='root',database='school')

#my_cur=db.cursor()



def welcome():
    root=Tk()
    root.title('SH \n CAFE')
    root.geometry('250x300')
    Label(root,text="Welcome to S H cafe", font='arial 16 bold').grid(row=0,columnspan=3)
    Label(root,text="").grid(row=1,column=0)
    Button(root,text="Billing",command=entry).grid(row=3,column=1)
   



def entry():
    root=Tk()
    root.title('SH \n CAFE')
    root.geometry('250x300')
    bg = PhotoImage(file = "C:\\Users\\harsh\\Downloads\\ok.png")
    Label( root, image = bg).pack
    Label(root,text="SH Cafe\nBilling", font='arial 16 bold').grid(row=0,columnspan=3)
    Label(root,text="").grid(row=1,column=0)
    Label(root,text="Cutomer name").grid(row=2,column=0)
    Label(root,text="").grid(row=3,column=0)
    Label(root,text="Contact Number").grid(row=4,column=0)
    Label(root,text="").grid(row=5,column=0)
    Button(root,text="Add Item").grid(row=6,column=1)
    Label(root,text="").grid(row=7,column=0)
    Label(root,text="Items ordered").grid(row=8,column=0)
    Label(root,text="").grid(row=9,column=0)
    Button(root,text="See Menu").grid(row=10,column=1)
    Label(root,text="").grid(row=11,column=0)
    v1=StringVar()
    e1=Entry(root,textvariable=v1).grid(row=2,column=1)
    v2=StringVar()
    e2=Entry(root,textvariable=v2).grid(row=4,column=1)
    v3=StringVar()
    e3=Entry(root,textvariable=v3).grid(row=8,column=1)

welcome()

engine = pyttsx3.init()
engine.say("Hello")
engine. setProperty("rate", 130)
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Welcome to S H Cafe")
engine. setProperty("rate", 130)
engine.runAndWait()
          
