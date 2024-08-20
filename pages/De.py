import sqlite3
from tkinter import messagebox

from PMS import Z


def De():
    zz = int(Z.get())
    conn = sqlite3.connect('PMS.db')
    
    # Fetch the necessary columns from the database
    cursor = conn.execute("SELECT REG, NAME, MOBILE, EMAIL, VEHICLE, PARK, TYPE, STATUS, SLOT, PB FROM PARKING")
    
    Flag = 0
    for row in cursor:
        # Check if the registration number matches and the 'PB' field is "P"
        if(row[0] == zz ):
            # Create the parking details string
            S = (f"PARKING DETAILS :\n"
                 f"REG. NO. = {row[0]}\n"
                 f"NAME = {row[1]}\n"  # Use correct indexes for fields
                 f"MOBILE = {row[2]}\n"
                 f"EMAIL = {row[3]}\n"
                 f"VEHICLE = {row[4]}\n"
                 f"PARKING = {row[5]}\n"
                 f"CATEGORY = {row[6]}\n"
                 f"STATUS = {row[7]}\n"
                 f"SLOT = {row[8]}\n")
            
            # Display the details in a message box
            messagebox.showinfo("Details", S)
            Flag = 1
    
    # If the registration number doesn't exist or parking is not booked
    if Flag == 0:
        S = "NOTE: Invalid Registration Number/Parking Not Booked"
        messagebox.showinfo("Note", S)
    
    conn.commit()
    conn.close()