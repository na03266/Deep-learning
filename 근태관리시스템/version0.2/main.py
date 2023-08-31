import tkinter as tk
from tkinter import messagebox
from controller.authentication_controller import AuthenticationController
from controller.attendance_controller import AttendanceController
from view.user_interface import UserInterface
from view.attendance_interface import AttendanceInterface

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("메인 메뉴")

        self.authentication_controller = AuthenticationController()
        self.attendance_controller = AttendanceController("version0.2/database/attendance.db")

        self.user_interface = UserInterface(self.root, self.authentication_controller)
        self.user_interface.login_button.config(command=self.login)

    def login(self):
        username = self.user_interface.username_entry.get()
        password = self.user_interface.password_entry.get()

        if self.authentication_controller.authenticate_user(username, password):
            self.root.destroy()
            attendance_root = tk.Tk()
            attendance_app = AttendanceInterface(attendance_root, self.attendance_controller, username)
            attendance_root.mainloop()
        else:
            messagebox.showerror("오류", "사용자 인증 실패!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
