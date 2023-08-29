import tkinter as tk
from tkinter import messagebox
from attendance.attendance_record import record_attendance
from authentication.db_handler import check_user_credentials

class UserAuthenticationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("사용자 인증 및 로그인")
        
        self.username_label = tk.Label(root, text="사용자명:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="비밀번호:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="로그인", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if check_user_credentials(username, password):
            self.open_attendance_interface(username)
        else:
            messagebox.showerror("오류", "사용자 인증 실패!")

    def open_attendance_interface(self, username):
        self.root.destroy()
        attendance_root = tk.Tk()
        app = UserAttendanceApp(attendance_root, username)
        attendance_root.mainloop()

class UserAttendanceApp:
    def __init__(self, root, username):
        self.root = root
        self.root.title("출퇴근 기록")

        self.username = username  # 사용자명 저장

        self.clock_in_button = tk.Button(root, text="출근", command=self.clock_in)
        self.clock_in_button.pack()

        self.clock_out_button = tk.Button(root, text="퇴근", command=self.clock_out)
        self.clock_out_button.pack()

    def clock_in(self):
        self.record("출근")

    def clock_out(self):
        self.record("퇴근")

    def record(self, status):
        username = self.username

        if username:
            record_attendance(username, status)
            messagebox.showinfo("성공", f"{status} 기록되었습니다.")
        else:
            messagebox.showerror("오류", "사용자명과 비밀번호를 입력해주세요.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserAuthenticationApp(root)
    root.mainloop()
