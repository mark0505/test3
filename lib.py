import json
import sqlite3

def 讀取帳密(file_path):
    """讀取並返回 JSON 檔案中的帳號密碼資訊。"""
    try:
        with open(file_path, 'r') as file:
            credentials = json.load(file)
        return credentials
    except FileNotFoundError:
        print("錯誤：找不到帳密檔案。")
        return None

def 驗證帳密(credentials, 使用者名稱, 密碼):
    """根據提供的使用者名稱和密碼進行身份驗證。"""
    if 使用者名稱 in credentials and credentials[使用者名稱] == 密碼:
        return True
    else:
        print("錯誤：使用者名稱或密碼錯誤。")
        return False

def 建立資料庫():
    """建立 SQLite3 資料庫並返回連線物件。"""
    try:
        connection = sqlite3.connect('wanghong.db')
        return connection
    except sqlite3.Error as e:
        print(f"錯誤：無法建立資料庫 - {e}")
        return None

def 建立會員資料表(connection):
    """在資料庫中建立 'members' 資料表。"""
    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS members (
                iid INTEGER PRIMARY KEY AUTOINCREMENT,
                mname TEXT NOT NULL,
                msex TEXT NOT NULL,
                mphone TEXT NOT NULL
            )
        ''')
        connection.commit()
        cursor.close()
    except sqlite3.Error as e:
        print(f"錯誤：無法建立 'members' 資料表 - {e}")

def 讀取會員檔案(file_path):
    """從文字檔案中讀取並返回會員資料。"""
    try:
        with open(file_path, 'r') as file:
            members_data = [line.strip().split(',') for line in file]
        return members_data
    except FileNotFoundError:
        print("錯誤：找不到會員檔案。")
        return None

def 匯入會員資料(connection, members_data):
    """將會員資料匯入 'members' 資料表。"""
    try:
        cursor = connection.cursor()
        cursor.executemany('INSERT INTO members (mname, msex, mphone) VALUES (?, ?, ?)', members_data)
        connection.commit()
        cursor.close()
        print("會員資料匯入成功。")
    except sqlite3.Error as e:
        print(f"錯誤：無法匯入會員資料 - {e}")

# 根據需要添加其他 CRUD 函數
