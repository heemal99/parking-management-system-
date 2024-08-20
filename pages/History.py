import sqlite3
from tkinter import messagebox


def History():
    S=""
    cott = sqlite3.connect('PPMS.db')
    cursor = cott.execute("SELECT REG,NAME,VEHICLE,PARK,TYPE,SLOT,C FROM PARKING")
    for row in cursor:
        S=S+str(row[0])+" - "+row[1]+" - "+row[2]+" - "+row[3]+" - "+row[4]+" - "+row[5]+"\n"
    messagebox.showinfo("Note",S)
    cott.commit()
    cott.close()