import sqlite3

DB_PATH = './db/bot_db.sqlite'

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Teams (
                        team_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        team_name TEXT NOT NULL,
                        points INTEGER DEFAULT 0
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Tasks (
                        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        task_name TEXT NOT NULL,
                        difficulty TEXT NOT NULL,
                        points INTEGER
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Submissions (
                        submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        team_id INTEGER,
                        task_id INTEGER,
                        status TEXT DEFAULT 'pending',
                        file_path TEXT,
                        FOREIGN KEY (team_id) REFERENCES Teams (team_id),
                        FOREIGN KEY (task_id) REFERENCES Tasks (task_id)
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Admins (
                        admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                      )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS TeamMembers (
                        member_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        team_id INTEGER,
                        member_name TEXT NOT NULL,
                        FOREIGN KEY (team_id) REFERENCES Teams (team_id)
                    )''')

    conn.commit()
    conn.close()
