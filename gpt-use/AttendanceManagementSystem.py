import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class AttendanceManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management System")
        
        self.attendance_data = {}  # 근태 데이터를 저장할 딕셔너리
        
        self.label = tk.Label(root, text="Enter Employee ID:")
        self.label.pack()

        self.employee_id_entry = tk.Entry(root)
        self.employee_id_entry.pack()

        self.mark_attendance_button = tk.Button(root, text="Mark Attendance", command=self.mark_attendance)
        self.mark_attendance_button.pack()

        self.show_attendance_button = tk.Button(root, text="Show Attendance", command=self.show_attendance)
        self.show_attendance_button.pack()

    def mark_attendance(self):
        employee_id = self.employee_id_entry.get()
        if employee_id:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if employee_id in self.attendance_data:
                self.attendance_data[employee_id].append(current_time)
            else:
                self.attendance_data[employee_id] = [current_time]
            
            messagebox.showinfo("Success", "Attendance marked for Employee ID: " + employee_id)
        else:
            messagebox.showerror("Error", "Please enter Employee ID")

    def show_attendance(self):
        employee_id = self.employee_id_entry.get()
        if employee_id:
            if employee_id in self.attendance_data:
                attendance_list = "\n".join(self.attendance_data[employee_id])
                messagebox.showinfo("Attendance for Employee ID: " + employee_id, attendance_list)
            else:
                messagebox.showinfo("Attendance for Employee ID: " + employee_id, "No attendance recorded")
        else:
            messagebox.showerror("Error", "Please enter Employee ID")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceManagementSystem(root)
    root.mainloop()
