import pymysql	
from tkinter import *
a6=pymysql.connect("localhost","root","12345","std1")
z1=a6.cursor()

def useridfun():
    global empid
    name1=m1.get()
    con1=m2.get()
    role1=m3.get()
    pass1=m4.get()
    sec1=m5.get()
    if z1.execute("select id from emp where name='{}' and pass='{}' and role='{}' and contact={} and security='{}'".format(name1,pass1,role1,con1,sec1)):
        res1=z1.fetchall()
        for row in res1:
            empid=row[0]
    
        Label(u,text="Your UserId is").grid(row=10,column=1)
        Label(u,text=empid).grid(row=10,column=2)
        Button(u,text="Redirect to Login",command=start).grid(row=16,column=2)
        
    else:
        Label(u,text="Wrong Details!!! Try Again...").grid(row=10,column=2)
    
    
    
def start():
    a6.commit()
    a6.close()
    u.withdraw()
    import main

def back():
    start()

    
    
def userid(a):
    global m1
    global u
    global m2
    global m3
    global m4
    global m5
    global m6
    u=Toplevel(a)
    u.title("Welcome To Account Section")
    u.geometry('400x400')
    u.resizable(1,1)
    Label(u,text="User Name",fg="red",bg="Yellow").grid(row=2,column=1)
    m1=Entry(u)
    m1.grid(row=2,column=2)
    Label(u,text="User Contact",fg="red",bg="Yellow").grid(row=3,column=1)
    m2=Entry(u)
    m2.grid(row=3,column=2)
    Label(u,text="User Role",fg="red",bg="Yellow").grid(row=4,column=1)
    m3=Entry(u)
    m3.grid(row=4,column=2)
    Label(u,text="Password",fg="black",bg="Yellow").grid(row=5,column=1)
    m4=Entry(u,show="*")
    m4.grid(row=5,column=2)
    Label(u,text="Security Question",fg="black",bg="Yellow").grid(row=6,column=1)
    Label(u,text="What is yourFavourite Genre",fg="black",bg="Yellow").grid(row=7,column=1)
    m5=Entry(u,show="*")
    m5.grid(row=7,column=2)
    Button(u,text="Submit",command=useridfun).grid(row=8,column=2)
    Button(u,text="Back",command=back).grid(row=1,column=4)
    
