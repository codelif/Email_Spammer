import string
import os
import random
import yagmail

# Destination Email
destin = "friendsmail@notsponsored.com"

# For importing the credentials
mail = open("email.txt", "r").read()
pwd = open("pwd.txt", "r").read()

# Setting up yagmail and host is not required for gmail accounts
SMTP =  yagmail.SMTP(user=mail,password=pwd, host="smtp.gmail.com")

# For storing number of times email has been sent.
sent_times = 1

# While Loop so emails keep getting sent. To stop it most terminals have Ctrl+C shortcut to stop any running programming but you can also try doing Ctrl+Z if that doesn't Work
while True:
    SMTP.send(to=destin,subject=''.join(random.choice(string.ascii_lowercase) for i in range(10)),contents="Main Body", attachments=None, cc=None, bcc=None)
    print("Mail has been sent {} times").format(sent_times)
    sent_times+=1
