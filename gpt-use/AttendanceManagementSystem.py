import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from tkcalendar import DateEntry

class AttendanceManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        
        self.attendance_data = {}  # 근태 데이터를 저장할 딕셔너리
        self.user_data = {"admin": {"password": "admin123", "role": "admin"},
                          "employee": {"password": "employee123", "role": "employee"}}
        
        self.label_id = tk.Label(root, text="Enter User ID:")
        self.label_id.pack()

        self.user_id_entry = tk.Entry(root)
        self.user_id_entry.pack()

        self.label_password = tk.Label(root, text="Enter Password:")
        self.label_password.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        self.label_date = tk.Label(root, text="Select Date:")
        self.label_date.pack()

        self.selected_date = DateEntry(root, date_pattern="yyyy-mm-dd")
        self.selected_date.pack()

        self.show_attendance_button = tk.Button(root, text="Show My Attendance", command=self.show_attendance)
        self.show_attendance_button.pack()

        self.role = ""
        
    def login(self):
        user_id = self.user_id_entry.get()
        password = self.password_entry.get()
        
        if user_id and password:
            if user_id in self.user_data:
                if self.user_data[user_id]["password"] == password:
                    self.role = self.user_data[user_id]["role"]
                    self.show_main_menu()
                else:
                    messagebox.showerror("Error", "Invalid password")
            else:
                messagebox.showerror("Error", "Invalid user ID")
        else:
            messagebox.showerror("Error", "Please enter user ID and password")

    def show_main_menu(self):
        self.label_id.pack_forget()
        self.user_id_entry.pack_forget()
        self.label_password.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()

        if self.role == "admin":
            self.show_admin_menu()
        elif self.role == "employee":
            self.show_employee_menu()

    def show_admin_menu(self):
        self.label_date.pack()
        self.selected_date.pack()
        self.show_attendance_button.pack()

    def show_employee_menu(self):
        self.label_date.pack()
        self.selected_date.pack()
        self.show_attendance_button.pack()

    def show_attendance(self):
        selected_date_str = self.selected_date.get_date().strftime("%Y-%m-%d")
        user_id = self.user_id_entry.get()
        if user_id:
            if user_id in self.attendance_data:
                attendance_list = [time for time in self.attendance_data[user_id] if selected_date_str in time]
                if attendance_list:
                    attendance_info = "\n".join(attendance_list)
                    messagebox.showinfo("Attendance for User ID: " + user_id + " on " + selected_date_str, attendance_info)
                else:
                    messagebox.showinfo("Attendance for User ID: " + user_id + " on " + selected_date_str, "No attendance recorded on selected date")
            else:
                messagebox.showinfo("Attendance for User ID: " + user_id + " on " + selected_date_str, "No attendance recorded")
        else:
            messagebox.showerror("Error", "Please enter User ID")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceManagementSystem(root)
    root.mainloop()
