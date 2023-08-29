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
def create_attendance_table():
    conn = sqlite3.connect("attendance_database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY,
            username TEXT,
            status TEXT,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()

def record_attendance(username, status):
    create_attendance_table()  # 테이블이 없으면 생성
    # 나머지 record_attendance 함수 내용은 그대로 유지