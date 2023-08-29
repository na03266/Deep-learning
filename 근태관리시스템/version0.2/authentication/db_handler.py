import sqlite3

def check_user_credentials(username, password):
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()

    # 사용자 정보를 데이터베이스에서 조회
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    stored_password = cursor.fetchone()

    conn.close()

    if stored_password and stored_password[0] == password:
        return True
    return False
