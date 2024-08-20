from tkinter import messagebox

from PMS import Base_Page, SuperUser_GUI


def SptoBp():
    messagebox.showinfo("Status","Successfully Logged Off")
    SuperUser_GUI.destroy()
    Base_Page()