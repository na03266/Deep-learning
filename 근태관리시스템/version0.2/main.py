import tkinter as tk
from tkinter import messagebox
from authentication.user_authentication import authenticate_user
from interface.user_interface import UserAttendanceApp


class UserLoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("사용자 로그인")

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("메인 메뉴")

        self.login_button = tk.Button(root, text="로그인", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if authenticate_user(username, password):
            self.open_attendance_interface(username)
        else:
            messagebox.showerror("오류", "사용자 인증 실패!")

    def open_attendance_interface(self, username):
        self.root.destroy()
        attendance_root = tk.Tk()
        attendance_app = UserAttendanceApp(attendance_root, username)
        attendance_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
