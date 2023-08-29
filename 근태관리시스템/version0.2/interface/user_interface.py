import tkinter as tk
from tkinter import messagebox
from attendance.attendance_record import record_attendance

class UserAttendanceApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("출퇴근 기록")

        self.username = username

        self.clock_in_button = tk.Button(root, text="출근", command=self.clock_in)
        self.clock_in_button.pack()

        self.clock_out_button = tk.Button(root, text="퇴근", command=self.clock_out)
        self.clock_out_button.pack()

    def clock_in(self):
        record_attendance(self.username, "출근")

    def clock_out(self):
        record_attendance(self.username, "퇴근")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserAttendanceApp(root, "admin")  # 여기에 사용자명 입력
    root.mainloop()
