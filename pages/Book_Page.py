from tkinter import Button, Entry, Label, PhotoImage, Radiobutton, StringVar, Tk
from PMS import CalPrice2, CalPrice4, Park, User_GUI


def Book_Page():
    
    User_GUI.destroy()
    global Book_GUI
    Book_GUI=Tk()
    Book_GUI.title("Book Parking")
    w, h = Book_GUI.winfo_screenwidth(),Book_GUI.winfo_screenheight()
    Book_GUI.geometry("%dx%d+0+0" % (w, h))
    icon=PhotoImage(file="image.png")
    logo=Label(Book_GUI,image=icon)
    PMS=Label(Book_GUI,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=3)

    lab1=Label(Book_GUI,text="Reg. No.",padx=20,pady=5,font=("Times New Roman",32))
    lab2=Label(Book_GUI,text="Vehicle. No.",padx=20,pady=5,font=("Times New Roman",32))
    lab3=Label(Book_GUI,text="Parking",padx=20,pady=5,font=("Times New Roman",32))
    lab4=Label(Book_GUI,text="Category",padx=20,pady=5,font=("Times New Roman",32))
    lab5=Label(Book_GUI,text="Price",padx=20,pady=5,font=("Times New Roman",32))
    global Reg
    global Veh
    Reg=Entry(Book_GUI,font=("Times New Roman",32))
    Veh=Entry(Book_GUI,font=("Times New Roman",32))
    global var
    var = StringVar()
    R1 = Radiobutton(Book_GUI, text="B Block", variable=var, value="B Block",font=("Times New Roman",32))
    R2 = Radiobutton(Book_GUI, text="A Block", variable=var, value="A Block",font=("Times New Roman",32))
    global VehTyp
    VehTyp = StringVar()
    R3 = Radiobutton(Book_GUI, text="Two Wheeler", variable=VehTyp, value="2 Wheeler",command=CalPrice2,font=("Times New Roman",32))
    R4 = Radiobutton(Book_GUI, text="Four Wheeler", variable=VehTyp, value="4 Wheeer",command=CalPrice4,font=("Times New Roman",32))
    
    
    Book_Button=Button(Book_GUI,text="Book Now",command=Park,font=("Times New Roman",32))
    
    lab1.grid(row=2,column=0)
    Reg.grid(row=2,column=1)

    lab2.grid(row=3,column=0)
    Veh.grid(row=3,column=1)

    lab3.grid(row=4,column=0)
    R1.grid(row=4,column=1)
    R2.grid(row=4,column=2)

    lab4.grid(row=5,column=0)
    R3.grid(row=5,column=1)
    R4.grid(row=5,column=2)

    lab5.grid(row=6,column=0)
    global amt
    amt = Label(Book_GUI,font=("Times New Roman",32))
    amt.grid(row=6,column=1)
    
    Book_Button.grid(row=7,columnspan=2)
    
    Book_GUI.mainloop()