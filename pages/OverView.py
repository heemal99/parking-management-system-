import sqlite3
from tkinter import messagebox


def OverView():
    S=""
    conn = sqlite3.connect('PMS.db')
    cursor = conn.execute("SELECT REG,NAME,VEHICLE,PARK,TYPE,SLOT,C FROM PARKING")
    for row in cursor:
        if(row[6]=="C"):
            S=S+str(row[0])+" - "+row[1]+" - "+row[2]+" - "+row[3]+" - "+row[4]+" - "+row[5]+"\n"
    messagebox.showinfo("Note",S)
    conn.commit()
    conn.close()