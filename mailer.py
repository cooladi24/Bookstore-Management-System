# Open GMAIL, Go to setting > Security > Allow Less Secure Apps

import smtplib
import pymysql
a10=pymysql.connect("localhost","root","12345","std1")
b10=a10.cursor()



def mailfunc(e_id,b_id,b_name,b_price):
   global a
   a=e_id
   if b10.execute('select emailid from emp where id={}'.format(a)):
      res=b10.fetchall()
      for row in res:
         mail=row[0]

      EMAIL="adityadps24@gmail.com"
      PASSWORD="aditya24121998"
      TO=mail
      message = "Subject : Confirmation for Successful Book Purchase Transaction\n\n  Hello Sir/Madam,\n Thanks for purchasing the book from our MegaBook Store.Your transaction details are as below: \n Bookname:'{}'\n BookId:{}\n BookPrice:{}\n We will be happy to serve you again..!!\n If this transaction has not been performed from your membership card then kindly report at the store counter.\n\n Thanks & Regards\n MegaBook Store".format(b_name,b_id,b_price)
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
