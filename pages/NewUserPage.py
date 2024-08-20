from tkinter import Button, Entry, Label, PhotoImage, Tk

import Display_Users
from PMS import DB_Reg


def NewUser_Page():
    global NewUser_GUI
    NewUser_GUI = Tk()
    NewUser_GUI.title("User Registration Page")
    w, h = NewUser_GUI.winfo_screenwidth(), NewUser_GUI.winfo_screenheight()
    NewUser_GUI.geometry(f"{w}x{h}+0+0")
    
    icon = PhotoImage(file="image.png")
    logo = Label(NewUser_GUI, image=icon)
    PMS = Label(NewUser_GUI, text="Parking Management System", font=("Helvetica", 62))
    
    logo.grid(row=1, column=0)
    PMS.grid(row=1, column=1, columnspan=3, sticky="ew")
    
    labels = ["Name", "Reg. No.", "Mobile", "Email ID", "User Name", "Password"]
    for i, text in enumerate(labels, start=2):
        Label(NewUser_GUI, text=text, padx=20, pady=5, font=("Times New Roman", 23)).grid(row=i, column=0)
    
    global Name, Register, Mobile, Email, UserName, Pass
    Name = Entry(NewUser_GUI, font=("Times New Roman", 23))
    Register = Entry(NewUser_GUI, font=("Times New Roman", 23))
    Mobile = Entry(NewUser_GUI, font=("Times New Roman", 23))
    Email = Entry(NewUser_GUI, font=("Times New Roman", 23))
    UserName = Entry(NewUser_GUI, font=("Times New Roman", 23))
    Pass = Entry(NewUser_GUI, font=("Times New Roman", 23), show="*")
    
    Name.grid(row=2, column=1)
    Register.grid(row=3, column=1)
    Mobile.grid(row=4, column=1)
    Email.grid(row=5, column=1)
    UserName.grid(row=6, column=1)
    Pass.grid(row=7, column=1)
    
    Submit_Button = Button(NewUser_GUI, text="Submit", command=DB_Reg, font=("Times New Roman", 25), bd=3)
    Submit_Button.grid(row=8, column=1)
    
    Display_Button = Button(NewUser_GUI, text="Display Users", command=Display_Users, font=("Times New Roman", 25), bd=3)
    Display_Button.grid(row=9, column=1)
    
    NewUser_GUI.configure()
    NewUser_GUI.mainloop()