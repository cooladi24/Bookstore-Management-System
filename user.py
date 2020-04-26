import pymysql
import datetime
from mailer import *

from tkinter import *
a2=pymysql.connect("localhost","root","12345","std1")
b1=a2.cursor()

def searchfunc():
    if b1.execute("select * from book where bookname='{}'".format(sname.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
    
    elif b1.execute("select * from book where bookid={} and bookname='{}'".format(scode.get(),sname.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
            
    elif b1.execute("select * from book where bookid={}".format(scode.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
            
    
    else:
       Label(b,text="No.. Book Not Available in the library").grid(row=24,column=2)
       

def func():
    
        global b;
        global b_id
        global b_name
        global b_price
        global e_id
    
        if b1.execute("select * from book where bookid={} and bookname='{}'".format(bid.get(),bname.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            
            global e_bal
            if (e_bal-b_price>0):
                                        
                    Label(b,text="Thanks for Purchasing Book - '{}' and Your remaining balance is {} \nPlease press Back to buy another book else LogOut".format(b_name,(e_bal-b_price))).grid(row=7,column=1)
                    x = datetime.datetime.now()
                    x=str(x)
                    x=x.split()
                                       
                    e_bal-=b_price
                    print(e_bal)
                    b_quan-=1
                    print(e_bal,e_id)
                    b1.execute("update emp set bal={} where id={}".format(e_bal,e_id))
                    b1.execute("update book set quantity={} where bookid={}".format(b_quan,b_id))
                    b1.execute("insert into transdata values('{}',{},{},{},'{}',{},'{}','{}')".format(e_name,e_id,e_phone,b_id,b_name,b_price,x[0],x[1]))
                    Label(b,text="Name: '{}', Id: {}, Role: '{}', Bal: {}".format(e_name,e_id,e_role,e_bal),fg="red",bg="Yellow").grid(row=3,column=1)
                    a2.commit()
                    mailfunc(e_id,b_id,b_name,b_price)
                    
                    
            else:
                    Label(b,text="Purchase Failed..\nPlease press back and try again",fg='green',bg='white').grid(row=7,column=1)
            
        else:
                Label(b,text="Book not found in Database..\nPlease press back and try again",fg='green',bg='white').grid(row=7,column=1)
        
        
def lib1():
    global b
    b.withdraw()
    user(e_id,e_pass,b)

def exitfunc1():
    global b
    a2.close()
    b.withdraw()
    import main



def user(eid,epass,a):
    global b
    global e_role
    
    b=Toplevel(a)
    b.title("User Section")
    b.geometry('480x480')
    b.resizable(1,1)
    Label(b,text="Welcome To The User Section",fg="red",bg="Yellow").grid(row=1,column=2)
    b1.execute("select * from emp where id={} and pass='{}'".format(eid,epass))
    res=b1.fetchall()
    global e_id
    global e_name
    global e_pass
    global e_bal
    global e_phone
    for row in res:
         e_name=row[0]
         e_id=row[1]
         e_pass=row[2]
         e_role=row[3]
         e_bal=row[4]
         e_phone=row[6]
    Label(b,text="Name: '{}', Id: {}, Role: '{}', Bal: {}".format(e_name,e_id,e_role,e_bal),fg="red",bg="Yellow").grid(row=3,column=1)
    Label(b,text="Book Id").grid(row=4,column=1)
    global bid
    bid=Entry(b)
    bid.grid(row=4,column=2)
    Label(b,text="Book Name").grid(row=5,column=1)
    global bname
    bname=Entry(b)
    bname.grid(row=5,column=2)
    Button(b,text="Submit",command=func).grid(row=6,column=2)
    Button(b,text="Back",command=lib1).grid(row=1,column=5)
    Button(b,text="LogOut",command=exitfunc1).grid(row=1,column=6)
    Label(b,text="Available Books Are:").grid(row=11,column=1)
    i=1
    b1.execute("select * from book where quantity > 0")
    myresult=b1.fetchall()
    listdata=Listbox(b)
    for x in myresult:
               
            listdata.insert(i,x)
            i=i+1
    listdata.grid(row=13,column=1)

    Label(b,text="Book Code").grid(row=20,column=1)
    global scode
    scode=Entry(b)
    scode.grid(row=20,column=2)
    Label(b,text="Book Name").grid(row=21,column=1)
    global sname
    sname=Entry(b)
    sname.grid(row=21,column=2)
    Button(b,text="Search",command=searchfunc).grid(row=22,column=2)
