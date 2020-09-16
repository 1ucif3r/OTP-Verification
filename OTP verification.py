import tkinter as tk
from tkinter import messagebox
from twilio.rest import Client
import random
otp=random.randint(9999,100000)
otp=str(otp)

def check():
    userentry=y.get()
    if otp==userentry:
        messagebox.showinfo("showinfo","Login success")
    else:
        messagebox.showinfo("showinfo","Incorrect OTP")

def sendsms():
    number = x. get()

    client= Client('SSID','TOKEN')

    client.messages.create(from_='twilio no',to=number,body='Your OTP is '+otp)

    messagebox.showinfo("showninfo","OTP has been sent....")
    root.destroy()
    win=tk.Tk()
    win.geometry("300x200")
    global y
    y=tk.StringVar()
    l1=tk.Label(win,text="Enter Your OTP")
    l1.place(x=10,y=5)
    e1=tk.Entry(win,textvariable=y)
    e1.place(x=10,y=30,height=30,width=250)
    b1=tk.Button(win,text='Submit',fg='white',bg='#202020')
    b1.place(x=10,y=80)

root=tk.Tk()
root.geometry('300x200')
root.title('OTP Verification')
x=tk.StringVar()
l=tk.Label(root,text='Enter your mobile no with Country code')
l.place(x=10,y=5)
e = tk.Entry(root)
e.place(x=10,y=30,height=39,width=250)
b=tk.Button(root,text='Send OTP',fg='white',bg='#202020',command=sendsms)
b.place(x=10,y=80)

root.mainloop()
