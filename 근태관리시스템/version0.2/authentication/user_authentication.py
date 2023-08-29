import tkinter as tk
from tkinter import messagebox
from authentication.db_handler import check_user_credentials
from interface.user_interface import UserAttendanceApp

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
            messagebox.showerror("오류", "사용자명 또는 비밀번호가 잘못되었습니다.")

    def open_attendance_interface(self, username):
        self.root.destroy()
        attendance_root = tk.Tk()
        attendance_app = UserAttendanceApp(attendance_root, username)
        attendance_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = UserAuthenticationApp(root)
    root.mainloop()
