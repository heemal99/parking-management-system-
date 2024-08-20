import sqlite3
from tkinter import BOTH, LEFT, RIGHT, VERTICAL, Button, Canvas, Frame, Label, Scrollbar, Toplevel, messagebox


def Display_Users():
    def delete_user(reg_no):
        if reg_no:
            conn = sqlite3.connect('PMS.db')
            conn.execute("DELETE FROM PARKING WHERE REG=?", (reg_no,))
            conn.commit()
            conn.close()
            
            messagebox.showinfo("Status", f"User with Registration Number {reg_no} Deleted Successfully")
            update_user_list()

    def update_user_list():
        for widget in display_frame.winfo_children():
            widget.destroy()
        
        conn = sqlite3.connect('PMS.db')
        cursor = conn.execute("SELECT * FROM PARKING")
        users = cursor.fetchall()
        conn.close()
        
        headers = ["Reg. No.", "Name", "Mobile", "Email", "Username", "Delete"]
        for col, text in enumerate(headers):
            header_label = Label(display_frame, text=text, font=("Helvetica", 14, "bold"), bg="#f0f0f0", fg="#333333", relief="solid", padx=10, pady=10)
            header_label.grid(row=0, column=col, sticky="nsew")
        
        for i, user in enumerate(users):
            user_info = [user[0], user[1], user[2], user[3], user[4]]
            for col, info in enumerate(user_info):
                info_label = Label(display_frame, text=info, font=("Helvetica", 12), bg="#ffffff", fg="#000000", padx=10, pady=10)
                info_label.grid(row=i + 1, column=col, sticky="w")
            
            delete_button = Button(display_frame, text="Delete", command=lambda reg_no=user[0]: delete_user(reg_no), font=("Helvetica", 12), relief="flat", padx=10, pady=5)
            delete_button.grid(row=i + 1, column=len(user_info), sticky="e")
    
    display_window = Toplevel()
    display_window.title("All Registered Users")
    display_window.geometry("1000x600")
    
    display_window.configure(bg="#f0f0f0")
    
    canvas = Canvas(display_window, bg="#f0f0f0")
    scrollbar = Scrollbar(display_window, orient=VERTICAL, command=canvas.yview)
    display_frame = Frame(canvas, bg="#f0f0f0")
    
    canvas.create_window((0, 0), window=display_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    display_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    update_user_list()