from user import *
import datetime
import time
from userid import *
from admin import *
from mailer2 import *
from librarian import *
import pymysql	
from tkinter import *
from mailer import *
from mailer1 import *
from forgotpass import *
a1=pymysql.connect("localhost","root","12345","std1")
b=a1.cursor()

def confirmfun():
    esecans=m11.get()
    if b.execute("update emp set security='{}' where id={}".format(esecans,eid11)):
        Label(a11,text="Security Key updated Successfully").grid(row=6,column=2)
        Button(a11,text="Login Again",command=tostart).grid(row=7,column=2)
    else:
        Label(a11,text="Security Key updation failed.. Try Again").grid(row=6,column=2)
        Button(a11,text="Login Again",command=tostart).grid(row=7,column=2)

def tostart():
    a1.commit()
    a1.close()
    a.withdraw()
    a11.withdraw()
    import main
    
    

def secfunc():
    global a11
    global a
    global m11
    global esec11
    global eid11
    ids=int(m1.get())
    passw=m2.get()
    b.execute("select id,name,security from emp where id={} and pass='{}'".format(ids,passw))
    res1=b.fetchall()
    for row in res1:
        eid11=row[0]
        ename11=row[1]
        esec11=row[2]
    if esec11:
        fun()
    else:
        a11=Tk()
        a11.title("Security Key Settings")
        a11.geometry('500x500')
        a11.resizable(0,0)
        Label(a11,text="User Id - {}, Name - '{}'".format(eid11,ename11),fg="red",bg="Yellow").grid(row=1,column=1)
        Label(a11,text="Security Question..").grid(row=2,column=1)
        Label(a11,text="What is your Favourite Genre").grid(row=3,column=1)
        m11=Entry(a11)
        m11.grid(row=3,column=2)
        Button(a11,text="Submit",command=confirmfun).grid(row=5,column=2)
        Button(a11,text="Back",command=tostart).grid(row=1,column=3)
    


    
def fun():
    global a
    ids=m1.get()
    passw=m2.get()
    
    
    if b.execute("select * from emp where id={} and pass='{}'".format(ids,passw)):
        Label(a,text="Access Granted..").grid(row=6,column=1)
        
        res=b.fetchall()
        for row in res:
            ename=row[0]
            eid=row[1]
            epass=row[2]
            erole=row[3]
            ebal=row[4]
        if(erole=='user'):
            a.withdraw()
            user(eid,epass,a)
        elif(erole=='admin'):
            a.withdraw()
            admin(eid,epass,a)
        elif(erole=='librarian'):
            a.withdraw()
            librarian(eid,epass,a)
    else:
        Label(a,text="Wrong Details!!! Try Again...").grid(row=6,column=2)
    x = datetime.datetime.now()
    x=str(x)
    x=x.split()
    b.execute("delete from transdata where date1 < DATE_SUB('{}',INTERVAL 6 MONTH)".format(x[0]))
    a1.commit()
    a1.close()

def funcall():
    global a
    a.withdraw()
    userid(a)

def funcall1():
    global a
    a.withdraw()
    passset(a)
    
def startfunc():
    
    global m1
    global a
    global m2
    a=Tk()
    a.title("Welcome To MegaBookStore")
    a.geometry('400x400')
    a.resizable(0,0)
    Label(a,text="User Id",fg="red",bg="Yellow").grid(row=1,column=1)
    m1=Entry(a)
    m1.grid(row=1,column=2)
    Label(a,text="Password",fg="black",bg="Yellow").grid(row=2,column=1)
    m2=Entry(a,show="*")
    m2.grid(row=2,column=2)
    Label(a,text="(Max 10 Characters)").grid(row=3,column=1)
    Button(a,text="Submit",command=secfunc).grid(row=4,column=2)
    Button(a,text="Forgot Password",command=funcall1).grid(row=6,column=2)
    Button(a,text="Forgot UserId",command=funcall).grid(row=7,column=2)    

startfunc()
