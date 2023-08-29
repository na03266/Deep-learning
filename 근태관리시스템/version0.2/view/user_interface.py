import tkinter as tk
from tkinter import messagebox

class UserInterface:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("사용자 인터페이스")
        self.controller = controller

        self.root.geometry("300x250")  # 윈도우 크기 조정

        self.username_label = tk.Label(root, text="사용자명:")
        self.username_label.pack(pady=10)  # 위젯과 위젯 사이 간격 조정

        self.username_entry = tk.Entry(root)
        self.username_entry.pack(pady=5)  # 위젯과 위젯 사이 간격 조정

        self.password_label = tk.Label(root, text="비밀번호:")
        self.password_label.pack(pady=10)  # 위젯과 위젯 사이 간격 조정

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)  # 위젯과 위젯 사이 간격 조정

        self.register_button = tk.Button(root, text="회원 가입", command=self.register)
        self.register_button.pack(pady=5)  # 위젯과 위젯 사이 간격 조정

        self.login_button = tk.Button(root, text="로그인", command=self.login)
        self.login_button.pack(pady=5)  # 위젯과 위젯 사이 간격 조정

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            user = self.controller.register_user(username, password)
            messagebox.showinfo("성공", f"{user.username}님, 회원 가입이 완료되었습니다.")
        else:
            messagebox.showerror("오류", "사용자명과 비밀번호를 입력하세요.")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.controller.authenticate_user(username, password):
            messagebox.showinfo("성공", "로그인 성공!")
        else:
            messagebox.showerror("오류", "사용자 인증 실패!")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserInterface(root, None)
    root.mainloop()
