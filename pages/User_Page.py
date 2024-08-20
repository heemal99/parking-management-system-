from tkinter import Button, Entry, Label, PhotoImage, Tk
from PMS import Book_Page, De, Login_GUI, UptoBp


def User_Page():
    Login_GUI.destroy()
    global User_GUI
    User_GUI=Tk()
    w,h=User_GUI.winfo_screenwidth(),User_GUI.winfo_screenheight()
    User_GUI.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="image.png")
    logo=Label(User_GUI,image=icon)
    PMS=Label(User_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)

    icon1=PhotoImage(file="Book.png")
    Book=Label(User_GUI,image=icon1)
    BookParking_Button=Button(User_GUI,text="Book Parking",font=("Times New Roman",32),bd=3,command=Book_Page)
    icon3=PhotoImage(file="Logout.png")
    Logout=Label(User_GUI,image=icon3)
    Logout_Button=Button(User_GUI,text="Logout",font=("Times New Roman",32),bd=3,command=UptoBp)

    icon4=PhotoImage(file="Parking.png")
    Y=Label(User_GUI,text="Registration No.",font=("Times New Roman",28),padx=20,pady=5)
    global Z
    Z=Entry(User_GUI,font=("Times New Roman",28))
    Details=Label(User_GUI,image=icon4)
    Details_Button=Button(User_GUI,text="Details",font=("Times New Roman",32),bd=3,command=De)
    
    Book.grid(row=2)
    BookParking_Button.grid(row=3,column=0)
    
    Logout.grid(row=2,column=2)
    Logout_Button.grid(row=3,column=2)
    Details.grid(row=2,column=3)
    Y.grid(row=3,column=3)
    Z.grid(row=4,column=3)
    Details_Button.grid(row=5,column=3)
    User_GUI.mainloop()
    User_GUI.mainloop()