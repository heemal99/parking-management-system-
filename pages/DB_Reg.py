import sqlite3
from tkinter import messagebox
from PMS import Base_Page, Email, Mobile, Name, NewUser_GUI, Pass, Register, UserName


def DB_Reg():
    
    dbReg=int(Register.get())
    dbName=str(Name.get())
    dbMobile=str(Mobile.get())
    dbEmail=str(Email.get())
    dbUserName=str(UserName.get())
    dbPass=str(Pass.get())
    dbVehicle=str("NIL")
    dbPark=str("NIL")
    dbType=str("NIL")
    dbStatus=str("Not Parked")
    dbSlot=str("NIL")
    dbPb=str("NIL")
    if(str(Register.get())=="" or str(Name.get())=="" or str(Mobile.get())==""  or str(Email.get())=="" or str(UserName.get())=="" or str(Pass.get())==""):
        messagebox.showinfo("Warning", "Fields can not be Empty !!!")
    else:
        conn = sqlite3.connect('PMS.db')
        cott = sqlite3.connect('PPMS.db')
        cursor=conn.execute("INSERT INTO PARKING (REG,NAME,MOBILE,EMAIL,USERNAME,PASSWORD,VEHICLE,PARK,TYPE,STATUS,SLOT,PB) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(dbReg,dbName,dbMobile,dbEmail,dbUserName,dbPass,dbVehicle,dbPark,dbType,dbStatus,dbSlot,dbPb))
        conn.commit()
        cursor=cott.execute("INSERT INTO PARKING (REG,NAME,MOBILE,EMAIL,USERNAME,PASSWORD,VEHICLE,PARK,TYPE,STATUS,SLOT,PB) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",(dbReg,dbName,dbMobile,dbEmail,dbUserName,dbPass,dbVehicle,dbPark,dbType,dbStatus,dbSlot,dbPb))
        cott.commit()
        messagebox.showinfo("Status", "Successfully Registered\nUse the User Name & Password to Login")
        NewUser_GUI.destroy()
        Base_Page()