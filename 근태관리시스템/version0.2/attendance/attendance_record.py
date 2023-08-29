import sqlite3
from datetime import datetime

def record_attendance(username, status):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect("attendance_database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO attendance (username, status, timestamp) VALUES (?, ?, ?)", (username, status, now))
    conn.commit()

    conn.close()
