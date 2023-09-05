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

    def register_user(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register User")

        label_id = tk.Label(register_window, text="Enter New User ID:")
        label_id.pack()

        new_user_id_entry = tk.Entry(register_window)
        new_user_id_entry.pack()

        label_password = tk.Label(register_window, text="Enter Password:")
        label_password.pack()

        new_password_entry = tk.Entry(register_window, show="*")
        new_password_entry.pack()

        label_role = tk.Label(register_window, text="Select Role:")
        label_role.pack()

        roles = ["admin", "employee"]
        role_var = tk.StringVar()
        role_var.set(roles[0])  # Default role

        role_dropdown = tk.OptionMenu(register_window, role_var, *roles)
        role_dropdown.pack()

        register_button = tk.Button(register_window, text="Register", command=lambda: self.register_user_action(new_user_id_entry.get(), new_password_entry.get(), role_var.get(), register_window))
        register_button.pack()

    def register_user_action(self, user_id, password, role, register_window):
        if user_id and password:
            if user_id not in self.user_data:
                self.user_data[user_id] = {"password": password, "role": role}
                messagebox.showinfo("Success", "User registered successfully")
                register_window.destroy()
            else:
                messagebox.showerror("Error", "User ID already exists")
        else:
            messagebox.showerror("Error", "Please enter User ID and password")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceManagementSystem(root)
    root.mainloop()
