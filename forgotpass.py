import pymysql	
from tkinter import *
from mailer1 import *
a5=pymysql.connect("localhost","root","12345","std1")
z=a5.cursor()

def forgfun():
    global pass1
    pass1=m5.get()
    pass2=m6.get()
    global ans
    if pass1==pass2:
        
        Label(m,text="Security Question..").grid(row=10,column=1)
        Label(m,text="Name your Favourite Genre..").grid(row=12,column=1)
        ans=Entry(m)
        ans.grid(row=12, column=2)
        Button(m,text="Submit",command=seccheck).grid(row=13,column=2)

def seccheck():
    global x
    x=m1.get()
    z.execute("select security from emp where id={} and name='{}'".format(m1.get(),m2.get()))
    res=z.fetchall()
    for row in res:
        esecurity=row[0]
    if esecurity==ans.get():
        z.execute("update emp set pass='{}' where id={}".format(pass1,m1.get()))
        mailfunc1(x)
        Label(m,text="Password Updated Successfully..").grid(row=14,column=2)
        Button(m,text="Redirect to Login",command=start).grid(row=16,column=2)
        
    else:
        Label(a,text="Wrong Details!!! Try Again...").grid(row=14,column=2)
    a5.commit()
    

def start():
    global m
    a5.close()
    m.withdraw()
    import main

def back():
    start()

    
    
def passset(a):
    global m1
    global m
    global m2
    global m3
    global m4
    global m5
    global m6
    m=Toplevel(a)
    m.title("Welcome To Account Section")
    m.geometry('400x400')
    m.resizable(1,1)
    Label(m,text="User Id",fg="red",bg="Yellow").grid(row=1,column=1)
    m1=Entry(m)
    m1.grid(row=1,column=2)
    Label(m,text="User Name",fg="red",bg="Yellow").grid(row=2,column=1)
    m2=Entry(m)
    m2.grid(row=2,column=2)
    Label(m,text="User Contact",fg="red",bg="Yellow").grid(row=3,column=1)
    m3=Entry(m)
    m3.grid(row=3,column=2)
    Label(m,text="User Role",fg="red",bg="Yellow").grid(row=4,column=1)
    m4=Entry(m)
    m4.grid(row=4,column=2)
    Label(m,text="New Password",fg="black",bg="Yellow").grid(row=5,column=1)
    m5=Entry(m,show="*")
    m5.grid(row=5,column=2)
    Label(m,text="Confirm Password",fg="black",bg="Yellow").grid(row=6,column=1)
    m6=Entry(m,show="*")
    m6.grid(row=6,column=2)
    Label(m,text="(Max 10 Characters)").grid(row=7,column=1)
    Button(m,text="Submit",command=forgfun).grid(row=8,column=2)
    Button(m,text="Back",command=back).grid(row=1,column=4)
    
