import pymysql
import datetime
from mailer import *

from tkinter import *
a3=pymysql.connect("localhost","root","12345","std1")
b2=a3.cursor()

def insfunc():
    if b2.execute("insert into emp(name,id,pass,role,contact,emailid) values('{}',{},'{}','{}',{},'{}')".format(ename1.get(),eid1.get(),epass1.get(),erole1.get(),econ1.get(),eemail.get())):
        Label(c,text="Inserted Successfully",fg='green',bg='white').grid(row=19,column=1)
        
        a3.commit()
        
            
    else:
        Label(c,text="Insertion Failed!!! Try Again...",fg='green',bg='white').grid(row=19,column=1)

def searchfunc():
    if b2.execute("select * from book where bookname='{}'".format(sname.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)

    elif b2.execute("select * from book where bookid={}".format(scode.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
              

    elif b2.execute("select * from book where bookid={} and bookname='{}'".format(scode.get(),sname.get())):
            res=b2.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(c,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
            

    else:
       Label(c,text="No.. Book Not Available in the library").grid(row=24,column=2)
       



def insertfunc():
    if b2.execute("insert into book(bookid,bookname,quantity) values({},'{}',0)".format(bid.get(),bname.get())):
        Label(c,text="Book Inserted Successfully",fg='green',bg='white').grid(row=16,column=1)
        b2.execute("select * from book")
        res=b2.fetchall()
        for row in res:
            b_id=row[0]
            b_name=row[1]
            print(b_id,b_name)
        a3.commit()
        
            
    else:
        Label(c,text="Insertion Failed!!! Try Again...",fg='green',bg='white').grid(row=16,column=1)

def deletefunc():
    if b2.execute("delete from emp where id={} and name='{}'".format(eid2.get(),ename2.get())):
        Label(c,text="User Deleted Successfully",fg='green',bg='white').grid(row=16,column=1)        
        b2.execute("select * from emp")
        res=b2.fetchall()
        for row in res:
            e_id=row[0]
            e_name=row[1]
            print(e_id,e_name)
        a3.commit()
        
    else:
        Label(c,text="Deletion Failed!!! Try Again...",fg='green',bg='white').grid(row=16,column=1)

    

def delfunc():
    if b2.execute("delete from book where bookid={} and bookname='{}'".format(bid.get(),bname.get())):
        Label(c,text="Book Deleted Successfully",fg='green',bg='white').grid(row=16,column=1)        
        b2.execute("select * from book")
        res=b2.fetchall()
        for row in res:
            b_id=row[0]
            b_name=row[1]
            print(b_id,b_name)
        a3.commit()
    
    else:
        Label(c,text="Deletion Failed!!! Try Again...",fg='green',bg='white').grid(row=16,column=1)

def function():
    
    ch1=sel.get()
    if (int(ch1)==1):
        
        Label(c,text="Id of Book",fg="black",bg="Yellow").grid(row=12,column=1)
        global bid
        bid=Entry(c)
        bid.grid(row=12,column=2)
        Label(c,text="Name of Book",fg="black",bg="Yellow").grid(row=13,column=1)
        global bname
        bname=Entry(c)
        bname.grid(row=13,column=2)
        Button(c,text="Submit",command=insertfunc).grid(row=14,column=3)

    elif (int(ch1)==2):
        
        Label(c,text="Id of Book",fg="black",bg="Yellow").grid(row=12,column=1)
        global bid0
        bid0=Entry(c)
        bid0.grid(row=12,column=2)
        Label(c,text="Name of Book",fg="black",bg="Yellow").grid(row=13,column=1)
        global bname0
        bname0=Entry(c)
        bname0.grid(row=13,column=2)
        Button(c,text="Submit",command=delfunc).grid(row=14,column=3) 
    
    elif (int(ch1)==3):
        
        Label(c,text="Id Of User",fg="black",bg="Yellow").grid(row=12,column=1)
        global eid1
        eid1=Entry(c)
        eid1.grid(row=12,column=2)
        Label(c,text="Name Of User",fg="black",bg="Yellow").grid(row=13,column=1)
        global ename1
        ename1=Entry(c)
        ename1.grid(row=13,column=2)
        Label(c,text="Role Of User",fg="black",bg="Yellow").grid(row=14,column=1)
        global erole1
        erole1=Entry(c)
        erole1.grid(row=14,column=2)
        Label(c,text="Contact No.",fg="black",bg="Yellow").grid(row=15,column=1)
        global econ1
        econ1=Entry(c)
        econ1.grid(row=15,column=2)
        Label(c,text="Pass Of User",fg="black",bg="Yellow").grid(row=16,column=1)
        global epass1
        epass1=Entry(c)
        epass1.grid(row=16,column=2)
        Label(c,text="Email Of User",fg="black",bg="Yellow").grid(row=17,column=1)
        global eemail
        eemail=Entry(c)
        eemail.grid(row=17,column=2)
        Button(c,text="Submit",command=insfunc).grid(row=18,column=3)

    elif (int(ch1)==4):
        
        Label(c,text="Id of User",fg="black",bg="Yellow").grid(row=12,column=1)
        global eid2
        eid2=Entry(c)
        eid2.grid(row=12,column=2)
        Label(c,text="Name of User",fg="black",bg="Yellow").grid(row=13,column=1)
        global ename2
        ename2=Entry(c)
        ename2.grid(row=13,column=2)
        Button(c,text="Submit",command=deletefunc).grid(row=14,column=3) 

    elif (int(ch1)==5):
        Label(c,text="Transaction List:").grid(row=20,column=1)
        i=1
        b2.execute("select * from transdata")
        myresult=b2.fetchall()
        listdata=Listbox(c)
        for x in myresult:
            listdata.insert(i,x)
            i=i+1
        listdata.grid(row=22,column=2)
        


def confirm1():
    ch=m1.get()
    if (int(ch)==1):
        Label(c,text="1 for Adding Book, 2 for Deleting Book",fg="black",bg="Yellow").grid(row=8,column=1)
        Label(c,text="3 for Adding User, 4 for Deleting User",fg="black",bg="Yellow").grid(row=9,column=1)
        Label(c,text="5 for Transaction List",fg="black",bg="Yellow").grid(row=10,column=1)
        global sel
        sel=Entry(c)
        sel.grid(row=8,column=3)
        Button(c,text="Submit",command=function).grid(row=11,column=3)
        
    else:
        Label(c,text="Book Id").grid(row=8,column=1)
        global bid1
        bid1=Entry(c)
        bid1.grid(row=8,column=2)
        Label(c,text="Book Name").grid(row=9,column=1)
        global bname1
        bname1=Entry(c)
        bname1.grid(row=9,column=2)
        Button(c,text="Submit",command=userfunc11).grid(row=10,column=2)
        Label(c,text="Available Books Are:").grid(row=15,column=1)
        i=1
        b2.execute("select bookid,bookname,price from book where quantity > 0")
        myresult=b2.fetchall()
        listdata=Listbox(c)
        for x in myresult:
            listdata.insert(i,x)
            i=i+1
        listdata.grid(row=15,column=2)

        Label(c,text="Book Code").grid(row=20,column=1)
        global scode
        scode=Entry(c)
        scode.grid(row=20,column=2)
        Label(c,text="Book Name").grid(row=21,column=1)
        global sname
        sname=Entry(c)
        sname.grid(row=21,column=2)
        Button(c,text="Search",command=searchfunc).grid(row=22,column=2)

        

def userfunc11():
        global b_id
        global b_name
        global b_price
        global e_id
          
        if b2.execute("select * from book where bookid={} and bookname='{}'".format(bid1.get(),bname1.get())):
            res=b2.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            
            global ebal
            if (ebal-b_price>0):
                                        
                    Label(c,text="Thanks for Purchasing Book - '{}' and Your remaining balance is {}".format(b_name,(ebal-b_price))).grid(row=12,column=1)
                    x = datetime.datetime.now()
                    x=str(x)
                    x=x.split()        
                    ebal-=b_price
                    print(ebal)
                    b_quan-=1
                    print(ebal,e_id)
                    b2.execute("insert into transdata values('{}',{},{},{},'{}',{},'{}','{}')".format(ename,e_id,e_phone,b_id,b_name,b_price,x[0],x[1]))
                    b2.execute("update emp set bal={} where id={}".format(ebal,e_id))
                    b2.execute("update book set quantity={} where bookid={}".format(b_quan,b_id))
                    Label(c,text="Name: '{}', Id: {}, Role: '{}', Bal: {}".format(ename,e_id,erole,ebal),fg="red",bg="Yellow").grid(row=2,column=1)
                    x = datetime.datetime.now()
                    x=str(x)
                    x=x.split()
                    b2.execute("delete from transdata where date1 < DATE_SUB('{}',INTERVAL 6 MONTH)".format(x[0]))
                    mailfunc(e_id,b_id,b_name,b_price)
                     
            else:
                    Label(c,text="Purchase Failed",fg='green',bg='white').grid(row=13,column=1)
            a3.commit()
            
        else:
                Label(c,text="Book not found in Database",fg='green',bg='white').grid(row=13,column=1)

    
                
        
def lib2():
    global c
    c.withdraw()
    admin(e_id,e_pass,c)


def exitfunc2():
    global c
    a3.close()
    c.withdraw()
    import main
    


def admin(eid,epass,a):
    
    global c
    global e_pass
    global ename
    global e_id
    global e_phone
    global erole
    global ebal
    c=Toplevel(a)
    c.title("Admin Section")
    c.geometry('625x625')
    c.resizable(1,1)
    Label(c,text="Welcome To The Admin Section",fg="red",bg="Yellow").grid(row=1,column=2)
    b2.execute("select * from emp where id={} and pass='{}'".format(eid,epass))
    res=b2.fetchall()
    for row in res:
        ename=row[0]
        e_id=row[1]
        e_pass=row[2]
        erole=row[3]
        ebal=row[4]
        e_phone=row[6]
    Label(c,text="Name: '{}', Id: {}, Role: '{}', Bal: {}".format(ename,e_id,erole,ebal),fg="red",bg="Yellow").grid(row=2,column=1)
    Label(c,text="Do you Continue as Admin Or as an User").grid(row=3,column=1)
    Label(c,text="Press 1 for Admin Or 2 for User").grid(row=4,column=1)
    global m1
    m1=Entry(c)
    m1.grid(row=4,column=2)
    Button(c,text="Submit",command=confirm1).grid(row=6,column=2)    
    Button(c,text="Back",command=lib2).grid(row=1,column=7)
    Button(c,text="LogOut",command=exitfunc2).grid(row=1,column=8)
