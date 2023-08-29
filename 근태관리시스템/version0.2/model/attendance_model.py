import datetime

class AttendanceRecord:
    def __init__(self, username, status):
        self.username = username
        self.status = status
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"Username: {self.username}, Status: {self.status}, Timestamp: {self.timestamp}"
