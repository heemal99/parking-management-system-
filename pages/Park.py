import sqlite3
from tkinter import messagebox
from numpy import var
from PMS import Base_Page, Book_GUI, Reg, Veh, VehTyp


def Park():
    dbR = str(Reg.get())  # Registration number
    dbV = str(Veh.get())  # Vehicle information
    dbA = str(var.get())  # Parking area
    dbT = str(VehTyp.get())  # Vehicle type

    if dbR == "" or dbV == "" or dbA == "" or dbT == "":
        messagebox.showinfo("Warning", "Fields Cannot Be Empty !!!")
    else:
        conn = sqlite3.connect('PMS.db')
        cursor = conn.execute("SELECT REG, VEHICLE, PARK, TYPE, STATUS FROM PARKING")
        
        

        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Status", "Successfully Booked Parking")
        Book_GUI.destroy()
        Base_Page()