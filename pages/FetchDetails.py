import sqlite3
from tkinter import messagebox

from matplotlib.pyplot import show
from PMS import Z, Z1


def FetchDetails():
    if(str(Z.get())=="" and str(Z1.get())=="" ):
       S="Please Fill - Registration/Vehicle"
       messagebox.showinfo("Warning",S)
       return
    
    if(str(Z.get())==""):
        zz=0
    else:
        zz=int(Z.get())
    v=str(Z1.get())
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT REG,NAME,SEX,MOBILE,EMAIL,VEHICLE,PARK,TYPE,STATUS,SLOT  FROM PARKING")
    Flag=0
    for row in cursor:
        if(row[0]==zz or row[6]==v):
            S="PARKING DETAILS : \nREG. NO. = "+str(row[0])+"\nNAME = "+row[2]+"\nGENDER = "+row[4]+"\nMOBILE = "+row[3]+"\nEMAIL = "+row[5]+"\nVEHICLE = "+row[6]+"\nPARKING = "+row[7]+"\nCATEGORY = "+row[8]+"\nSTATUS = "+row[9]+"\nSLOT = "+row[10]+"\n\n"
            messagebox.showinfo("Details",S)
            show()
            Flag=1
    if(Flag==0):
        S="NOTE : Invalid Details Provided/Parking Not Booked"
        messagebox.showinfo("Note",S)
    conn.commit()
