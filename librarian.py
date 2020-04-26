import pymysql
import datetime
from mailer2 import *
from tkinter import *
from mailer import *
a4=pymysql.connect("localhost","root","12345","std1")
b3=a4.cursor()

def func6():
    global eid
    global amt
    global addm
    global zid
    zid=int(eid.get())
    addm=int(bal.get())
    amt=e_bal+int(bal.get())
    x = datetime.datetime.now()
    x=str(x)
    x=x.split()
    b3.execute("delete from transdata where date1 < DATE_SUB('{}',INTERVAL 6 MONTH)".format(x[0]))
    b3.execute("update emp set bal={} where id={}".format((e_bal+int(bal.get())),int(eid.get())))
    a4.commit()
    mailfunc2(addm,amt,zid)
    
    Label(d,text="Updated Balance",fg='green',bg='white').grid(row=16,column=1)
        


    

def func5():
    
    global b_quan
    if b3.execute("select price,quantity from book where bookid={} and bookname='{}'".format(int(bid.get()),bname.get())):
        res=b3.fetchall()
        print(b3.execute("select price,quantity from book where bookid={} and bookname='{}'".format(int(bid.get()),bname.get())))
        print(res)
        for row in res:
            b_price=row[0]
            b_quan=row[1]
        a=int(bquan.get())
        print(b_quan)
                
        b3.execute("update book set price={} where bookid={}".format(int(bprice.get()),int(bid.get())))
        b3.execute("update book set quantity={} where bookid={}".format((a+b_quan),int(bid.get())))
        Label(d,text="Updated Price and Quantity",fg='green',bg='white').grid(row=16,column=1)
        a4.commit()
        
    else:
        Label(d,text="Book doesn't Exist!!!",fg='green',bg='white').grid(row=16,column=1)
    

def func4():
    global eid
    global e_bal
    global bal
    b3.execute("select bal from emp where id={} and name='{}'".format(int(eid.get()),ename.get()))
    res=b3.fetchall()
    for row in res:
        e_bal=row[0]    
    Label(d,text="Update Balance",fg='green',bg='white').grid(row=14,column=1)
    bal=Entry(d)
    bal.grid(row=14,column=2)
    Button(d,text="Submit",command=func6).grid(row=15,column=1)

    

    

def func3():
    choice=int(m2.get())
    if choice==1:
        global eid
        global ename
        Label(d,text="Id of User",fg="black",bg="Yellow").grid(row=10,column=1)
        eid=Entry(d)
        eid.grid(row=10,column=2)
        Label(d,text="Name of User",fg="black",bg="Yellow").grid(row=11,column=1)
        ename=Entry(d)
        ename.grid(row=11,column=2)
        Button(d,text="Submit",command=func4).grid(row=12,column=1)

    elif choice==2:
        global bid
        global bname
        global bprice
        global bquan
        Label(d,text="Id of Book",fg="black",bg="Yellow").grid(row=10,column=1)
        bid=Entry(d)
        bid.grid(row=10,column=2)
        Label(d,text="Name of Book",fg="black",bg="Yellow").grid(row=11,column=1)
        bname=Entry(d)
        bname.grid(row=11,column=2)
        Label(d,text="Price of Book",fg="black",bg="Yellow").grid(row=12,column=1)
        bprice=Entry(d)
        bprice.grid(row=12,column=2)
        Label(d,text="Quantity of Book",fg="black",bg="Yellow").grid(row=13,column=1)
        bquan=Entry(d)
        bquan.grid(row=13,column=2)
        Button(d,text="Submit",command=func5).grid(row=14,column=1)

    elif choice==3:
        Label(d,text="Transaction List:").grid(row=15,column=1)
        i=1
        b3.execute("select * from transdata")
        myresult=b3.fetchall()
        listdata=Listbox(d)
        for x in myresult:
            listdata.insert(i,x)
            i=i+1
        listdata.grid(row=17,column=1)   
        
def userfunc():

        global b_id
        global b_name
        global b_price
        global e_id
    
        if b3.execute("select * from book where bookid={} and bookname='{}'".format(bid.get(),bname.get())):
            res=b3.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            
            global e_bal
            if (e_bal-b_price>0):
                                        
                    Label(d,text="Thanks for Purchasing Book - '{}' and Your remaining balance is {}".format(b_name,(e_bal-b_price))).grid(row=12,column=1)
                    x = datetime.datetime.now()
                    x=str(x)
                    x=x.split()   
                    e_bal-=b_price
                    print(e_bal)
                    b_quan-=1
                    print(e_bal,e_id)
                    b3.execute("update emp set bal={} where id={}".format(e_bal,e_id))
                    b3.execute("update book set quantity={} where bookid={}".format(b_quan,b_id))
                    b3.execute("insert into transdata values('{}',{},{},{},'{}',{},'{}','{}')".format(e_name,e_id,e_phone,b_id,b_name,b_price,x[0],x[1]))
                    Label(d,text="Name: '{}', Id: {}, Role: '{}', Bal: {}".format(e_name,e_id,e_role,e_bal),fg="red",bg="Yellow").grid(row=2,column=1)
                    a4.commit()
                    mailfunc(e_id,b_id,b_name,b_price)
                    
            else:
                    Label(d,text="Purchase Failed",fg='green',bg='white').grid(row=13,column=1)
            
        else:
                Label(d,text="Book not found in Database",fg='green',bg='white').grid(row=14,column=1)

def lib():
    global d
    d.withdraw()
    librarian(e_id,e_pass,d)

def exitfunc():
    global d
    a4.close()
    d.withdraw()
    import main


    
def confirm():
     global d

     c1=m1.get()
     if (int(c1)==1):
          
         Label(d,text="1 for Updating Balance, 2 for Updating Quantity and Price, 3 for Transaction List",fg="black",bg="Yellow").grid(row=7,column=1)
         global m2
         m2=Entry(d)
         m2.grid(row=8,column=1)
         Button(d,text="Submit",command=func3).grid(row=9,column=1)

     else:
         
         Label(d,text="Book Id").grid(row=8,column=1)
         global bid
         bid=Entry(d)
         bid.grid(row=8,column=2)
         Label(d,text="Book Name").grid(row=9,column=1)
         global bname
         bname=Entry(d)
         bname.grid(row=9,column=2)
         Button(d,text="Submit",command=userfunc).grid(row=10,column=2)
         Label(d,text="Available Books Are:").grid(row=15,column=1)
         i=1
         b3.execute("select * from book where quantity > 0")
         myresult=b3.fetchall()
         listdata=Listbox(d)
         for x in myresult:
             listdata.insert(i,x)
             i=i+1
         listdata.grid(row=17,column=1)

         
         Label(d,text="Book Code").grid(row=20,column=1)
         global scode
         scode=Entry(d)
         scode.grid(row=20,column=2)
         Label(d,text="Book Name").grid(row=21,column=1)
         global sname
         sname=Entry(d)
         sname.grid(row=21,column=2)
         Button(d,text="Search",command=searchfunc).grid(row=22,column=2)

    
def searchfunc():
    if b3.execute("select * from book where bookname='{}'".format(sname.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)

    elif b3.execute("select * from book where bookid={}".format(scode.get())):
            res=b1.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(b,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
              
    elif b3.execute("select * from book where bookid={} and bookname='{}'".format(scode.get(),sname.get())):
            res=b3.fetchall()
            for row in res:
                b_id=row[0]
                b_name=row[1]
                b_price=row[2]
                b_quan=row[3]
            Label(d,text="  Yes.. Book Available in the library   ").grid(row=24,column=2)
            

    else:
       Label(d,text="No.. Book Not Available in the library").grid(row=24,column=2)
       

        

def librarian(eid,epass,a):
    global d
    global m1
    global e_id
    global e_name
    global e_pass
    global e_role
    global e_phone
    global e_bal
    d=Toplevel(a)
    d.title("Accountant Section")
    d.geometry('600x600')
    d.resizable(1,1)
    Label(d,text="Welcome To The Accountant Section",fg="red",bg="Yellow").grid(row=1,column=2)
    Button(d,text="LogOut",command=exitfunc).grid(row=1,column=7)
    Button(d,text="Back",command=lib).grid(row=1,column=6)
    b3.execute("select * from emp where id={} and pass='{}'".format(eid,epass))
    res=b3.fetchall()
    for row in res:
        e_name=row[0]
        e_id=row[1]
        e_pass=row[2]
        e_role=row[3]
        e_bal=row[4]
        e_phone=row[6]
    Label(d,text="Name: '{}', Id: {}, Role: '{}', Bal: {}".format(e_name,e_id,e_role,e_bal),fg="red",bg="Yellow").grid(row=2,column=1)
    Label(d,text="Do you want to continue as Librarian or as an User").grid(row=4,column=1)
    Label(d,text="Press 1 for Librarian & 2 for User").grid(row=5,column=1)
    m1=Entry(d)
    m1.grid(row=5,column=2)
    Button(d,text="Submit",command=confirm).grid(row=6,column=1)
    
    
    
