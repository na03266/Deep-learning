import tkinter as tk
from tkinter import messagebox
from authentication.user_authentication import check_user_credentials
from interface.user_interface import UserAttendanceApp

class UserLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("사용자 로그인")

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

if __name__ == "__main__":
    root = tk.Tk()
    app = UserLoginApp(root)
    root.mainloop()
