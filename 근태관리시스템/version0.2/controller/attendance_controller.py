import sqlite3
import datetime
from model.attendance_model import AttendanceRecord

class AttendanceController:
    def __init__(self, db_path):
        self.db_path = db_path
        self.create_table()  # 테이블을 생성하도록 호출

    def create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS attendance_records (
                           id INTEGER PRIMARY KEY,
                           username TEXT NOT NULL,
                           status TEXT NOT NULL,
                           timestamp TIMESTAMP NOT NULL)''')

        conn.commit()
        conn.close()

    def record_attendance(self, username, status):
        timestamp = datetime.datetime.now()
        record = AttendanceRecord(username, status, timestamp)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO attendance_records (username, status, timestamp)
                          VALUES (?, ?, ?)''', (username, status, timestamp))

        conn.commit()
        conn.close()

        return record

    def get_user_records(self, username):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM attendance_records WHERE username=?''', (username,))
        rows = cursor.fetchall()

        conn.close()

        records = []
        for row in rows:
            id, username, status, timestamp = row
            record = AttendanceRecord(username, status, timestamp)
            records.append(record)

        return records
