import sqlite3
from tkinter import messagebox


def AvailSlots():
    S34=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    S29=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    A34=""
    A29=""
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT PARK,STATUS,SLOT FROM PARKING")
    for row in cursor:
        if(row[0]=="A Block" and row[1]=="Parked" and row[2]!="NIL"):
            S34[int(row[2])]=-1
        if(row[0]=="B Block" and row[1]=="Parked" and row[2]!="NIL"):
            S29[int(row[2])]=-1
    for i in S34:
        if(i!=-1 and i!=0):
            A34=A34+str(i)+" "
    for i in S29:
        if(i!=-1 and i!=0):
            A29=A29+str(i)+" "
    conn.commit()
    messagebox.showinfo("Status","Available Parking Slots\n\nBLOCK B ---- "+A29+"\n\nBLOCK A ----  "+A34)
