import tkinter as tk
from tkinter import messagebox

class AttendanceInterface:
    def __init__(self, root, controller, username):
        self.root = root
        self.controller = controller
        self.username = username
        self.root.title("근무 기록")

        self.root.geometry("300x400")  # 윈도우 크기 조정

        self.clock_in_button = tk.Button(root, text="출근", command=self.clock_in)
        self.clock_in_button.pack(pady=10)  # 위젯과 위젯 사이 간격 조정

        self.clock_out_button = tk.Button(root, text="퇴근", command=self.clock_out)
        self.clock_out_button.pack(pady=10)  # 위젯과 위젯 사이 간격 조정

        self.record_listbox = tk.Listbox(root)
        self.record_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)  # 레이아웃 및 간격 조정

        self.refresh_records()

    def clock_in(self):
        self.record("출근")

    def clock_out(self):
        self.record("퇴근")

    def record(self, status):
        record = self.controller.record_attendance(self.username, status)
        self.refresh_records()
        messagebox.showinfo("성공", f"{self.username}님의 {status} 기록이 완료되었습니다.")

    def refresh_records(self):
        self.record_listbox.delete(0, tk.END)
        records = self.controller.get_user_records(self.username)
        for record in records:
            self.record_listbox.insert(tk.END, str(record))

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceInterface(root, None, "admin")
    root.mainloop()
