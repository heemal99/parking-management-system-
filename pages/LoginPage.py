from logging import root
from tkinter import Button, Entry, Label, PhotoImage, Tk
from wsgiref import validate

from PMS import LptoNu


def Login_Page():
    root.destroy()
    global Login_GUI
    Login_GUI=Tk()
    Login_GUI.title("Login Page")
    w,h=Login_GUI.winfo_screenwidth(),Login_GUI.winfo_screenheight()
    Login_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="image.png")
    logo=Label(Login_GUI,image=icon)
    PMS=Label(Login_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=4)
    
    lab1=Label(Login_GUI,text="User Name",padx=20,pady=5,font=("Times New Roman",28))
    lab2=Label(Login_GUI,text="Password",padx=20,pady=5,font=("Times New Roman",28))
    lab3=Label(Login_GUI,text="\n",font=("Times New Roman",28))
    global name
    global pswd
    name=Entry(Login_GUI,font=("Times New Roman",28))
    pswd=Entry(Login_GUI,show="*",font=("Times New Roman",28))
    
    Login_Button=Button(Login_GUI,text=" Login  ",command=validate,font=("Times New Roman",32))
    NewUser_Button=Button(Login_GUI,text="Admin Panel",command=LptoNu,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=1)
    lab2.grid(row=3,column=1)
    name.grid(row=2,column=2)
    pswd.grid(row=3,column=2)
    lab3.grid(row=4)
    Login_Button.grid(row=5,column=1)
    NewUser_Button.grid(row=5,column=2)
    Login_GUI.mainloop()