 SMTP = Simple Mail Transfer Protocol, is a TCP/IP protocol used in sending and receiving email.
 
If wanted to send or recieve an email at time/at a particular action. We can use it.

Example:
  
import smtplib

my_email = "devopsmails1@gmail.com"
my_email_pwd = "darvcqkwahuswzvo" #should be the apppassword enabled on sending email account setting 

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_email_pwd)
    connection.sendmail(
        from_addr=my_email,
        to_addrs= "alamurilakshmiprasad@gmail.com",
        msg="Subject:Boss\n\nConfirmation testing mail"
    )
