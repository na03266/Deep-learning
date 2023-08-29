import sqlite3

def save_to_database(user_info):
    try:
        conn = sqlite3.connect("user_database.db")
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (user_info["username"], user_info["password"]))

        conn.commit()
        print("사용자 정보를 데이터베이스에 저장했습니다.")
    except sqlite3.Error as e:
        print("데이터베이스 오류:", e)
    finally:
        conn.close()
