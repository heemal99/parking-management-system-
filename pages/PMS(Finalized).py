from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime

from LoginPage import Login_GUI
from NewUserPage import NewUser_Page
from PMS import Availability, Login_Page

conn = sqlite3.connect('PMS.db')
conn.execute("""CREATE TABLE IF NOT EXISTS PARKING (REG INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,MOBILE CHAR(12) NOT NULL,EMAIL CHAR(50) NOT NULL,
USERNAME CHAR(50) NOT NULL,PASSWORD CHAR(50) NOT NULL,VEHICLE CHAR(15) NOT NULL,PARK CHAR(10) NOT NULL, TYPE CHAR(12) NOT NULL ,STATUS CHAR(5) NOT NULL,SLOT CHAR(5) NOT NULL,PB CHAR(5) NOT NULL,C CHAR(5),CIN CHAR(50),COUT CHAR(50))""")
conn.commit()
conn.close()

conn = sqlite3.connect('PPMS.db')
conn.execute("""CREATE TABLE IF NOT EXISTS PARKING (REG INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,MOBILE CHAR(12) NOT NULL,EMAIL CHAR(50) NOT NULL,
USERNAME CHAR(50) NOT NULL,PASSWORD CHAR(50) NOT NULL,VEHICLE CHAR(15) NOT NULL,PARK CHAR(10) NOT NULL, TYPE CHAR(12) NOT NULL ,STATUS CHAR(5) NOT NULL,SLOT CHAR(5) NOT NULL,PB CHAR(5) NOT NULL,C CHAR(5),CIN CHAR(50),COUT CHAR(50))""")
conn.commit()
conn.close()


def Show():
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT * FROM PARKING")
    for row in cursor:
        print(row)
    conn.commit()
    conn.close()

def Base_Page():
    
    global root
    root=Tk()
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w,h))
    icon=PhotoImage(file="image.png")
    logo=Label(root,image=icon)
    PMS=Label(root,text="Parking Management System",font=("Helvetica", 62))
    logo.grid(row=1,column=0)
    PMS.grid(row=1,column=1,columnspan=2)
    
    icon1=PhotoImage(file="Login.png")
    Log=Label(root,image=icon1)
    Login_Button=Button(root,text="Login",font=("Times New Roman",32),bd=3,command=Login_Page)

    icon2=PhotoImage(file="NewUser.png")
    NUsr=Label(root,image=icon2)
    NewUser_Button=Button(root,text="Admin Panel",font=("Times New Roman",32),bd=3,command=BptoNu)
    icon3=PhotoImage(file="Availability.png")
    Avai=Label(root,image=icon3)
    Availability_Button=Button(root,text="Availability",font=("Times New Roman",32),bd=3,command=Availability)
    Log.grid(row=2)
    Login_Button.grid(row=3,column=0)
    NUsr.grid(row=2,column=1)
    NewUser_Button.grid(row=3,column=1)
    Avai.grid(row=2,column=2)
    Availability_Button.grid(row=3,column=2)
    root.mainloop()


def LptoNu():
    Login_GUI.destroy()
    NewUser_Page()
    
def BptoNu():
    root.destroy()
    NewUser_Page()
    
def validate():
    c=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT USERNAME,PASSWORD FROM PARKING")
    if((str(name.get())=="Admin" ) and (str(pswd.get())=="Admin")):    # If Username and Password is of Admin, Login as Admin
            c=2
    for row in cursor:
        if( (str(name.get())==row[0]) and (str(pswd.get())==row[1])):               # If Username & Password matches, Break & Proceed
            c=1
            break
        else:                                                                                                               # If doesn't match, Warning
            c=0
    if(c==1):
        messagebox.showinfo("Status", "Login Successful")
        User_Page()
    if(c==0):
        messagebox.showinfo("Status", "Login Failed.\nPlease Try Again")
    if(c==2):
        messagebox.showinfo("Status", "Admin Login")   
        LptoAdm()
    conn.commit()
        


import sqlite3
from tkinter import *
from tkinter import messagebox



def SuperUser_Page():
    global SuperUser_GUI
    SuperUser_GUI=Tk()
    w,h=SuperUser_GUI.winfo_screenwidth(),SuperUser_GUI.winfo_screenheight()
    SuperUser_GUI.geometry("%dx%d+0+0" % (w,h))

# Empty Laber at Column 1

    Emp=Label(SuperUser_GUI,text="                     ",font=("Times New Roman",17),padx=17,pady=5)
    Emp.grid(row=1,column=0)

# LPU Logo & Heading
    
    icon=PhotoImage(file="LPU-LogoDetails.png")
    logo=Label(SuperUser_GUI,image=icon)
    PMS=Label(SuperUser_GUI,text="Parking Management System",font=("Helvetica", 48))
    logo.grid(row=1,column=1)
    PMS.grid(row=1,column=2,columnspan=4)

# Parking Details

    icon1=PhotoImage(file="ParkingDetails.png")
    Details=Label(SuperUser_GUI,image=icon1)
    Y=Label(SuperUser_GUI,text="Registration No.",font=("Times New Roman",17),padx=17,pady=3)
    global Z
    Z=Entry(SuperUser_GUI,font=("Times New Roman",17))
    Y1=Label(SuperUser_GUI,text="Vehicle No.",font=("Times New Roman",17),padx=17,pady=3)
    global Z1
    Z1=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    Details_Button=Button(SuperUser_GUI,text="Fetch Details",font=("Times New Roman",15),bd=3,width=12,command=FetchDetails)

    

    Details.grid(row=2,column=1)
    Y.grid(row=3,column=1)
    Z.grid(row=4,column=1)
    Y1.grid(row=5,column=1)
    Z1.grid(row=6,column=1)
    
    Details_Button.grid(row=7,column=1,pady=4,rowspan=2)
   
    

# CheckIN

    icon2=PhotoImage(file="CheckIN.png")
    ChIN=Label(SuperUser_GUI,image=icon2)
    
    A=Label(SuperUser_GUI,text="Registration No.",font=("Times New Roman",17),padx=17,pady=3)
    global B
    B=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    A1=Label(SuperUser_GUI,text="Vehicle No.",font=("Times New Roman",17),padx=17,pady=3)
    global B1
    B1=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    A2=Label(SuperUser_GUI,text="Slot Number",font=("Times New Roman",17),padx=17,pady=3)
    global B2
    B2=Entry(SuperUser_GUI,font=("Times New Roman",17))

    R=Label(SuperUser_GUI,text="Block",font=("Times New Roman",25),padx=17,pady=3)
    global pd
    pd = StringVar()
    R1 = Radiobutton(SuperUser_GUI, text="B Block", variable=pd, value="B Block",font=("Times New Roman",17))
    R2 = Radiobutton(SuperUser_GUI, text="A Block", variable=pd, value="A Block",font=("Times New Roman",17))
    
    CheckIN_Button=Button(SuperUser_GUI,text="Check IN",font=("Times New Roman",17),bd=3,width=12,command=CheckIN)

    ChIN.grid(row=2,column=2,columnspan=2)
    A.grid(row=3,column=2,columnspan=2)
    B.grid(row=4,column=2,columnspan=2)
    A1.grid(row=5,column=2,columnspan=2)
    B1.grid(row=6,column=2,columnspan=2)
    A2.grid(row=7,column=2,columnspan=2)
    B2.grid(row=8,column=2,columnspan=2)
    R.grid(row=9,column=2,columnspan=2)
    R1.grid(row=10,column=2)
    R2.grid(row=10,column=3)
    CheckIN_Button.grid(row=11,column=2,columnspan=2)
    

# CheckOUT

    icon3=PhotoImage(file="CheckOUT.png")
    ChOUT=Label(SuperUser_GUI,image=icon3)
    
    C=Label(SuperUser_GUI,text="Registration No.",font=("Times New Roman",17),padx=17,pady=5)
    global D
    D=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    C1=Label(SuperUser_GUI,text="Vehicle No.",font=("Times New Roman",17),padx=17,pady=5)
    global D1
    D1=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    C2=Label(SuperUser_GUI,text="Slot Number",font=("Times New Roman",17),padx=17,pady=5)
    global D2
    D2=Entry(SuperUser_GUI,font=("Times New Roman",17))
    
    CheckOUT_Button=Button(SuperUser_GUI,text="Check OUT",font=("Times New Roman",17),bd=3,width=12,command=CheckOUT)

    ChOUT.grid(row=2,column=4)
    C.grid(row=3,column=4)
    D.grid(row=4,column=4)
    C1.grid(row=5,column=4)
    D1.grid(row=6,column=4)
    C2.grid(row=7,column=4)
    D2.grid(row=8,column=4)
    
    CheckOUT_Button.grid(row=10,column=4,rowspan=1)


# Other Features
    icon4=PhotoImage(file="Features.png")
    Feat=Label(SuperUser_GUI,image=icon4)
    OverView_Button=Button(SuperUser_GUI,text="Overview",font=("Times New Roman",17),bd=3,width=12,command=OverView)
    History_Button=Button(SuperUser_GUI,text="History",font=("Times New Roman",17),bd=3,width=12,command=History)
    Slots_Button=Button(SuperUser_GUI,text="Available Slots",font=("Times New Roman",17),bd=3,width=12,command=AvailSlots)
    Logout_Button=Button(SuperUser_GUI,text="Logout",font=("Times New Roman",17),bd=3,width=12,command=SptoBp)

    Feat.grid(row=2,column=5)
    OverView_Button.grid(row=4,column=5,pady=4)
    History_Button.grid(row=6,column=5,pady=4)
    Slots_Button.grid(row=8,column=5,pady=4)
    Logout_Button.grid(row=10,column=5)

    SuperUser_GUI.mainloop()



def CheckIN():
    if(str(B.get())=="" and str(B1.get())==""):
       S="Please Fill - Registration/Vehicle"
       messagebox.showinfo("Warning",S)
       return
    if((str(B.get())=="" or str(B1.get())=="" ) and str(B2.get())==""):
       S="Please Fill Slot Number"
       messagebox.showinfo("Warning",S)
       return
    if((str(B.get())=="" or str(B1.get())=="" ) and str(B2.get())!="" and str(pd.get())==""):
       S="Please Select Block"
       messagebox.showinfo("Warning",S)
       return
    
    if(str(B.get())==""):
        reg=0
    else:
        reg=int(B.get())
    veh=str(B1.get())
    slot=str(B2.get())
    blck=str(pd.get())
    
    
    Flag=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT REG,VEHICLE,STATUS,SLOT,PB,PARK  FROM PARKING")
    for row in cursor:
        if((row[0]==reg or row[1]==veh) and row[4]=="NIL"):
            S="NOTE : Book Parking First"
            messagebox.showinfo("Note",S)
            return
        if((row[0]==reg or row[1]==veh) and row[4]=="P" and row[2]=="Parked" ):
            S="NOTE : Vehicle Already Parked\nProceed With Checkout First"
            messagebox.showinfo("Note",S)
            return
        if((row[0]==reg or row[1]==veh) and row[4]=="P" and row[2]=="Not Parked" and row[5]==blck):          # Proceed with CheckIN
            Flag=1
            print("Proceed")
            break

    conn.commit()
    conn.close()    
    print("DB Close")
    if(Flag==1):
        conn = sqlite3.connect('PMS.db')
        cott = sqlite3.connect('PPMS.db')
        stateP=str("Parked")
        stateC=str("C")
        dbCin=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if(str(reg)!=0):
            conn.execute("UPDATE  PARKING SET SLOT=?, STATUS=?,C=?,CIN=? WHERE REG=?",(slot,stateP,stateC,dbCin,reg))
            cott.execute("UPDATE  PARKING SET SLOT=?, STATUS=?,C=?,CIN=? WHERE REG=?",(slot,stateP,stateC,dbCin,reg))
            S="NOTE : Vehicle Parked"
            messagebox.showinfo("Note",S)
        if(str(veh)!=""):
            conn.execute("UPDATE  PARKING SET SLOT=?, STATUS=?,C=?,CIN=? WHERE VEHICLE=?",(slot,stateP,stateC,dbCin,veh))
            cott.execute("UPDATE  PARKING SET SLOT=?, STATUS=?,C=?,CIN=? WHERE VEHICLE=?",(slot,stateP,stateC,dbCin,veh))
            S="NOTE : Vehicle Parked"
            messagebox.showinfo("Note",S)
        conn.commit()
        conn.close()
        cott.commit()
        cott.close()
    if(Flag==0):
        S="NOTE : Invalid Details/Block or Mismatching Entries"
        messagebox.showinfo("Note",S)
    Show()
    

    
    
        
def CheckOUT():
    if(str(D.get())=="" and str(D1.get())=="" and str(D2.get())==""):
       S="Please Fill - Registration/Vehicle/Slot"
       messagebox.showinfo("Warning",S)
       return
    
    if(str(D.get())==""):
        reg=0
    else:
        reg=int(D.get())
    veh=str(D1.get())
    slot=str(D2.get())
    
    
    Flag=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT REG,VEHICLE,STATUS,SLOT,PB  FROM PARKING")
    for row in cursor:
        if((row[0]==reg or row[1]==veh or row[3]==slot) and row[4]=="NIL"):
            S="NOTE : Book Parking First"
            messagebox.showinfo("Note",S)
            return
        if((row[0]==reg or row[1]==veh or row[3]==slot) and row[4]=="P" and row[2]=="Not Parked" ):
            S="NOTE : Vehicle Not Parked\nProceed With CheckIN First"
            messagebox.showinfo("Note",S)
            return
        if((row[0]==reg or row[1]==veh or row[3]==slot)  and row[4]=="P" and row[2]=="Parked"):          # Proceed with CheckOUT
            Flag=1
            print("Proceed out")
            break


    conn.commit()
    conn.close()
    print("DB Close")
    if(Flag==1):
        conn = sqlite3.connect('PMS.db')
        cott = sqlite3.connect('PPMS.db')
        stateP=str("Not Parked")
        stateS=str("NIL")
        stateC=str("")
        dbCout=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if(str(reg)!=0):
            conn.execute("UPDATE  PARKING SET STATUS=?,SLOT=?,C=?,COUT=? WHERE REG=?",(stateP,stateS,stateC,dbCout,reg))
            cott.execute("UPDATE  PARKING SET STATUS=?,SLOT=?,C=?,COUT=? WHERE REG=?",(stateP,stateS,stateC,dbCout,reg))
            S="NOTE : Vehicle Checked OUT"
            messagebox.showinfo("Note",S)
        if(str(veh)!=""):
            conn.execute("UPDATE  PARKING SET STATUS=?,SLOT=?,C=?,COUT=? WHERE VEHICLE=?",(stateP,stateS,stateC,dbCout,veh))
            cott.execute("UPDATE  PARKING SET STATUS=?,SLOT=?,C=?,COUT=? WHERE VEHICLE=?",(stateP,stateS,stateC,dbCout,veh))
            S="NOTE : Vehicle Cheked OUT"
            messagebox.showinfo("Note",S)
        if(str(slot)!=""):
            conn.execute("UPDATE  PARKING SET STATUS=?,SLOT=?,C=?,COUT=? WHERE SLOT=?",(stateP,stateS,stateC,dbCout,slot))
            cott.execute("UPDATE  PARKING SET STATUS=?,SLOT=?,C=?,COUT=? WHERE SLOT=?",(stateP,stateS,stateC,dbCout,slot))
            S="NOTE : Vehicle Cheked OUT"
            messagebox.showinfo("Note",S)
        conn.commit()
        conn.close()
        cott.commit()
        cott.close()
    Show()
    if(Flag==0):
        S="NOTE : Invalid Details or Mismatching Entries"
        messagebox.showinfo("Note",S)



Base_Page()###############################
