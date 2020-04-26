
# Open GMAIL, Go to setting > Security > Allow Less Secure Apps

import smtplib
import pymysql
a11=pymysql.connect("localhost","root","12345","std1")
b11=a11.cursor()



def mailfunc1(x):
   global a
   a=x
   if b11.execute('select emailid from emp where id={}'.format(a)):
      res=b11.fetchall()
      for row in res:
         mail=row[0]

      EMAIL="adityadps24@gmail.com"
      PASSWORD="aditya24121998"
      TO=mail
      message = "Subject : Change of your Account Password\n\n Hello Sir/Madam,\n Thanks for Changing the Password of your membership account at our MegaBook Store.\n We will be happy to serve you again..!!\n If this transaction has not been performed by you or the card holder then kindly report at the store counter.\n\n Thanks & Regards\n MegaBook Store"
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
