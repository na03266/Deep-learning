import tkinter as tk
from tkinter import messagebox
import os
import sys

# 현재 파일의 디렉토리를 기준으로 상대경로로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
attendance_dir = os.path.join(current_dir, "attendance")
sys.path.append(attendance_dir)

from attendance.attendance_record import record_attendance
class UserAttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("출퇴근 기록")

        self.username_label = tk.Label(root, text="사용자명:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="비밀번호:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.clock_in_button = tk.Button(root, text="출근", command=self.clock_in)
        self.clock_in_button.pack()

        self.clock_out_button = tk.Button(root, text="퇴근", command=self.clock_out)
        self.clock_out_button.pack()

    def clock_in(self):
        self.record("출근")

    def clock_out(self):
        self.record("퇴근")

    def record(self, status):
        username = self.username_entry.get()

        if username and self.password_entry.get():
            record_attendance(username, status)
            messagebox.showinfo("성공", f"{status} 기록되었습니다.")
        else:
            messagebox.showerror("오류", "사용자명과 비밀번호를 입력해주세요.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserAttendanceApp(root)
    root.mainloop()
