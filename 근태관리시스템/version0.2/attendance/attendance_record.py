import sqlite3
from datetime import datetime

def record_attendance(username, status):
    conn = sqlite3.connect("attendance_database.db")
    cursor = conn.cursor()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO attendance (username, status, timestamp) VALUES (?, ?, ?)", (username, status, now))

    conn.commit()
    conn.close()

def get_attendance_records(username):
    conn = sqlite3.connect("attendance_database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT status, timestamp FROM attendance WHERE username=?", (username,))
    records = cursor.fetchall()

    conn.close()
    return records
