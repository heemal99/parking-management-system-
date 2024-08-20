from tkinter import messagebox

from PMS import Base_Page, User_GUI


def UptoBp():
    messagebox.showinfo("Status","Successfully Logged Off")
    User_GUI.destroy()
    Base_Page()