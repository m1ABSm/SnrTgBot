import sqlite3
from config import DB_PATH
import os

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS inbox (
            number TEXT PRIMARY KEY,
            company TEXT,
            sender_name TEXT,
            email TEXT,
            subject TEXT,
            date TEXT
        )''')
        conn.commit()

def save_letter(data):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO inbox (number, company, sender_name, email, subject, date)
                       VALUES (?, ?, ?, ?, ?, DATE('now'))''',
                       (data['number'], data['company'], data['sender_name'], data['email'], data['subject']))
        conn.commit()

def get_last_number():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT number FROM inbox ORDER BY ROWID DESC LIMIT 1")
        row = cur.fetchone()
        return row[0] if row else None

def get_letter_by_number(number):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM inbox WHERE number = ?", (number,))
        return cur.fetchone()