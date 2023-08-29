import tkinter as tk
from interface.user_interface import UserAttendanceApp

if __name__ == "__main__":
    root = tk.Tk()
    app = UserAttendanceApp(root)
    root.mainloop()
