import sqlite3
from tkinter import messagebox


def Availability():
    Tot34=20
    Tot29=15
    C34=0
    C29=0
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT PARK FROM PARKING")
    for row in cursor:
        if(row[0]=="A Block"):
            C34=C34+1
        if(row[0]=="B Block"):
            C29=C29+1
    conn.commit()
    Av34=str(Tot34-C34)
    Av29=str(Tot29-C29)
    messagebox.showinfo("Status","Available Parking Slots\n\nBLOCK B ---- "+Av29+"\n\nBLOCK A ----  "+Av34)