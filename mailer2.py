# Open GMAIL, Go to setting > Security > Allow Less Secure Apps

import smtplib
import pymysql
a12=pymysql.connect("localhost","root","12345","std1")
b12=a12.cursor()



def mailfunc2(addm,amt,zid):
   global a
   a=zid
   if b12.execute('select emailid from emp where id={}'.format(a)):
      res=b12.fetchall()
      for row in res:
         mail=row[0]
      b12.execute('select name,role,contact from emp where id={}'.format(a))
      res=b12.fetchall()
      for row in res:
         name=row[0]
         role=row[1]
         cont=row[2]
         
         
      
      EMAIL="adityadps24@gmail.com"
      PASSWORD="aditya24121998"
      TO=mail
      message = "Subject : Updating Balance Transaction Successful\n\n Hello Sir/Madam,\n Your balance has been credited successfully with the recharge amount at our Megabook Store.Your transaction details are as below:\nName:'{}'\nUserId:{}\nRole:'{}'\nContact:{}\nCredit Amount:{}\nTotal Updated Balance:{}\n\n We will be happy to serve you again..!!\n If this transaction has not been performed by you or the card holder then kindly report at the store counter.\n\n Thanks & Regards\n MegaBook Store".format(name,a,role,cont,addm,amt)
      try:
         
         server = smtplib.SMTP('smtp.gmail.com:587')
         #smtpObj.sendmail(sender, receivers, message)         
         server.ehlo()
         server.starttls()
         server.login(EMAIL, PASSWORD)
         server.sendmail(EMAIL, TO, message)
         server.quit()
         print("Successfully sent email")
      except:
         print("Error: Unable to send email")
