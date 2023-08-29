import tkinter as tk
from tkinter import messagebox
from save_to_database import save_to_database  # save_to_database 모듈 임포트

class UserRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("회원 등록")
        
        self.username_label = tk.Label(root, text="사용자명:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="비밀번호:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="회원 등록", command=self.register)
        self.register_button.pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user_info = {"username": username, "password": password}
        save_to_database(user_info)

        messagebox.showinfo("성공", "회원 등록이 완료되었습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserRegistrationApp(root)
    root.mainloop()
