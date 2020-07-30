import string
import os
import random
import tkinter
import threading
import sys
os.system("pip install yagmail")
import yagmail

def spammer():
    # Destination Email
    destin = f"{destvalue.get()}"

    # For importing the credentials
    mail = f"{mailvalue.get()}"
    pwd = f"{pwdvalue.get()}"

    # Setting up yagmail and host is not required for gmail accounts
    SMTP =  yagmail.SMTP(user=mail,password=pwd, host="smtp.gmail.com")
    # For storing number of times email has been sent.
    sent_times = 1
    # While Loop so emails keep getting sent.
    while True:
        SMTP.send(to=destin,subject=''.join(random.choice(string.ascii_lowercase) for i in range(10)),contents="Main Body", attachments=None, cc=None, bcc=None)
        print(f"Mail has been sent {sent_times} times")
        sent_times+=1

def execute():
    t1 = threading.Thread(target=spammer)
    t1.daemon = True
    t1.start()

if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Email Spammer")
    root.geometry("350x100")

    tkinter.Label(root,text="Your Email").grid(row=0,column=2)
    tkinter.Label(root, text="Your Password").grid(row=1,column=2)
    tkinter.Label(root, text="Destination Email").grid(row=2,column=2)

    mailvalue = tkinter.StringVar()
    pwdvalue = tkinter.StringVar()
    destvalue = tkinter.StringVar()

    mailenter = tkinter.Entry(root,textvariable = mailvalue,width=40)
    pwdenter = tkinter.Entry(root,textvariable = pwdvalue,width=40)
    destenter = tkinter.Entry(root,textvariable = destvalue,width=40)

    mailenter.grid(row=0,column=3)
    pwdenter.grid(row=1,column=3)
    destenter.grid(row=2,column=3)

    tkinter.Button(root, text="Spam", command=execute).grid(row=3,column=2)

    root.mainloop()
    sys.exit()
