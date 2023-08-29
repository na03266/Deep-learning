import sqlite3

def check_user_credentials(username, password):
    conn = sqlite3.connect("user_database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    stored_password = cursor.fetchone()

    conn.close()

    if stored_password and stored_password[0] == password:
        return True
    return False
